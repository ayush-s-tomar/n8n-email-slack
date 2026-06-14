# n8n Email to Slack — AI Email Summarizer

An automation workflow that reads Gmail emails, summarizes them using Groq AI, and posts the summary to a Slack channel — fully automated, runs every minute.

## 🌐 Live Demo
Workflow running on n8n.cloud — connects Gmail → Groq AI → Slack automatically.

## 📸 What it does
- Receives a new email in Gmail
- Filters out newsletters and spam automatically
- Groq AI summarizes the email in 2-3 bullet points
- Posts the formatted summary to your Slack channel

## Features
- **Auto Filter** — Blocks noreply, newsletters, mailer-daemon emails
- **AI Summary** — LLaMA 3.1 summarizes emails with action items highlighted
- **Slack Notification** — Formatted message posted to any Slack channel
- **Runs Every Minute** — Fully automated, no manual trigger needed

## Tech Stack
| Layer | Tech |
|---|---|
| Automation | n8n |
| LLM | Groq API (LLaMA 3.1-8b-instant) |
| Email | Gmail API |
| Notifications | Slack API |
| Deployment | n8n Cloud |

## Project Structure
\```
n8n-email-slack/
├── workflow/
│   ├── email-to-slack-groq.json   # n8n workflow (Groq version)
│   └── email-to-slack.json        # n8n workflow (OpenAI version)
├── docs/
│   └── SETUP_GUIDE.md             # Step-by-step setup guide
└── main.py                        # Project entry point
\```

## Setup & Installation

### 1. Import the workflow
- Go to [n8n.cloud](https://n8n.cloud) and create a free account
- Click **New Workflow** → **Import from file**
- Upload `workflow/email-to-slack-groq.json`

### 2. Get your API keys
- Groq API key (free): [console.groq.com](https://console.groq.com)
- Gmail: Connect via Google OAuth in n8n
- Slack: Connect via Slack OAuth in n8n

### 3. Connect credentials
- **Gmail Trigger** → Sign in with Google
- **Groq AI Summarizer** → Header Auth → `Bearer your_groq_key`
- **Post to Slack** → Sign in with Slack → Select channel

### 4. Activate
Click **Publish** → workflow runs automatically every minute!

## How the Workflow Works
New Gmail Email

↓

[Filter Node]

Blocks spam/newsletters

↓

[Groq AI - LLaMA 3.1]

Summarizes in 2-3 bullet points

↓

[Slack Node]

Posts summary to #email-digest

## What I Learned
- Building no-code/low-code automation workflows with n8n
- Integrating Groq LLM API via HTTP Request nodes
- Gmail and Slack OAuth credential setup
- Workflow filtering and conditional logic in n8n

## License
MIT License — feel free to use and modify.

Built by Ayush Singh Tomar
