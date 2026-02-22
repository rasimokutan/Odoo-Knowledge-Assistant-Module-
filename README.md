Odoo RAG Knowledge Assistant (Offline AI Module)



Project Overview:

Odoo RAG Knowledge Assistant is a custom Odoo module that provides a lightweight, offline, AI-style chatbot experience inside Odoo ERP.
The module allows users to ask questions about Odoo concepts, modules, and workflows. Instead of using external APIs or cloud AI services, the system retrieves relevant information from a local knowledge base and displays context-based answers directly inside Odoo.
This project focuses on: custom Odoo module development, offline Retrieval-Augmented Generation (RAG) logic, simple and explainable AI-like architecture, and clean integration into ERP user experience.


What is RAG (Retrieval-Augmented Generation)?

RAG combines two steps: (1) Retrieval — finding relevant information from a knowledge source, and (2) Generation — creating a response using retrieved data instead of relying only on model memory.
Why use RAG? Traditional chatbots may hallucinate, cannot access custom company knowledge, and often depend on external services. RAG-based assistants use controllable data, produce consistent answers, and are easier to maintain.
In this project, retrieval is performed using a local knowledge file and generation is simplified by returning the most relevant retrieved content.


System Architecture

High-Level Architecture:
User Question
      ↓
Odoo Form Interface
      ↓
Python Model (Odoo ORM)
      ↓
RAG Engine
      ↓
Local Knowledge Base (TXT)
      ↓
Generated Response
      ↓
Displayed Inside Odoo


AI Flow (Step-by-Step)

1. User opens Odoo Knowledge Assistant
2. User writes a question
3. Ask button triggers Python method
4. RAG Engine loads knowledge base
5. Retrieval algorithm finds best matching chunks
6. System builds response
7. Answer appears in Odoo interface

   
Technologies Used

- Odoo 19.0 (ERP platform)
- Python (backend logic)
- XML (Odoo views & UI)
- PostgreSQL (database)
- VS Code (development environment)
- GitHub (version control)
- Local File System (knowledge base storage)

  
Development Environment

The module was developed locally using Odoo running on localhost, a Python environment, custom addon development workflow, and VS Code for coding/debugging.
Example addon path: odoo-19.0/addons/odoo_knowledge_assistant


Module Structure

odoo_knowledge_assistant/
│
├── __init__.py
├── __manifest__.py
│
├── models/
│   ├── assistant.py
│   └── rag_engine.py
│
├── views/
│   └── assistant_view.xml
│
├── security/
│   └── ir.model.access.csv
│
├── data/
│   └── qa_dataset.txt
Folder explanation: models = business logic and RAG backend; views = Odoo UI layouts; security = access permissions; data = local knowledge base.


Core Logic

assistant.py handles user question input, button action, calling the RAG engine, and writing the answer back to the form.
rag_engine.py loads the local dataset, splits content into chunks, compares user input with knowledge text, and returns best matches. This creates a simplified offline RAG pipeline.


Interface Overview

The assistant is fully integrated into Odoo as a regular module. Features include creating a new conversation, asking questions, retrieving answers from the knowledge base, and storing questions and answers as records.


Screenshots

1) Module Main Screen — main module page inside Odoo Applications.
2) New Question / Chat Screen — user creates a new record and types a question.
3) Example Answer (Modules Explanation) — assistant retrieves matching content.
4) Example Answer (Inventory Question) — retrieval-based response generation example.

   
Installation

1. Copy module into Odoo addons: addons/odoo_knowledge_assistant
2. Restart Odoo server (example: python odoo-bin -c odoo.conf)
3. In Odoo: Activate Developer Mode → Apps → Update Apps List → search 'Odoo Bilgi Asistanı' → Install

   
Usage

Open Odoo Knowledge Assistant → Assistant, click New, enter a question, press Ask, and view the generated answer.


Current Capabilities

- Offline RAG-like architecture
- Lightweight AI-style assistant
- Fully integrated Odoo module
- Local controllable data
- Simple and extendable structure

  
Future Improvements

- Embedding-based similarity search
- Vector database integration
- Local LLM support
- Better chunk ranking algorithms
- Automatic documentation ingestion
- Context memory between conversations

  
Design Philosophy

AI-assisted knowledge retrieval can be embedded directly into ERP systems using simple, explainable, and maintainable architecture.


Author

Custom Odoo module developed for learning and experimentation with AI-enhanced ERP workflows.


License

Educational / experimental project.
