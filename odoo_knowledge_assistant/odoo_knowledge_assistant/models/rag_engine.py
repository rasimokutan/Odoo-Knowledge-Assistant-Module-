import os
import re

from odoo import api, SUPERUSER_ID


KB_SECTIONS = []  # Uygulama açılırken yüklenecek


def _load_kb_file():
    """data/odoo_kb.txt dosyasını okuyup bölümlere ayırır."""
    global KB_SECTIONS
    if KB_SECTIONS:
        return  # Zaten yüklenmişse tekrar okuma

    module_dir = os.path.dirname(os.path.dirname(__file__))  # odoo_knowledge_assistant
    kb_path = os.path.join(module_dir, "data", "odoo_kb.txt")

    if not os.path.exists(kb_path):
        return

    with open(kb_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Bölümleri '### ' başlıklarına göre ayır
    # İlk split boş olabilir, onu filtreliyoruz
    raw_sections = re.split(r"^### ", content, flags=re.MULTILINE)
    sections = []
    for sec in raw_sections:
        sec = sec.strip()
        if not sec:
            continue
        # İlk satır başlık, gerisi açıklama
        lines = sec.splitlines()
        title = lines[0].strip()
        text = "\n".join(lines[1:]).strip()
        full_text = f"{title}\n{text}" if text else title
        sections.append(full_text)

    KB_SECTIONS = sections


def _tokenize(text):
    """Çok basit kelime parçalama ve temizleme."""
    # Küçük harfe çevir, harf ve sayıları bırak
    text = text.lower()
    # Türkçe karakterler kalsın diye sadece boşluklara göre bölelim
    tokens = re.split(r"\s+", text)
    # Noktalama işaretlerini temizle
    clean_tokens = [re.sub(r"[^\wçğıöşü]", "", t) for t in tokens]
    # Boş olanları at
    return set(t for t in clean_tokens if t)


def simple_retrieval(question, top_k=1):
    """
    Sorudaki kelimelerle bilgi tabanındaki bölümleri karşılaştırır.
    En benzer bölümü(leri) döndürür.
    """
    _load_kb_file()
    if not KB_SECTIONS:
        return ["Bilgi tabanı yüklenemedi. Lütfen odoo_kb.txt dosyasını kontrol edin."]

    q_tokens = _tokenize(question)
    if not q_tokens:
        return ["Lütfen daha anlamlı bir soru yazınız."]

    scored = []
    for section in KB_SECTIONS:
        s_tokens = _tokenize(section)
        if not s_tokens:
            continue
        common = q_tokens.intersection(s_tokens)
        # Basit benzerlik: ortak kelime sayısı
        score = len(common)
        if score > 0:
            scored.append((score, section))

    if not scored:
        return ["Sorunuzla ilgili bilgi tabanında uygun bir kayıt bulunamadı."]

    # Skora göre sırala, en yüksekten düşüğe
    scored.sort(key=lambda x: x[0], reverse=True)

    # top_k kadar sonucu döndür
    top_sections = [sec for score, sec in scored[:top_k]]
    return top_sections


def answer_question(question):
    """
    Dışarıdan çağrılan ana fonksiyon.
    Basit RAG mantığı: retrieve + cevabı birleştir.
    """
    sections = simple_retrieval(question, top_k=2)
    # Bölümleri alt alta birleştirerek cevap olarak dön
    return "\n\n---\n\n".join(sections)
