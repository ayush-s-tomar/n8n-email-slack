# Email → AI Summary → Slack — n8n Setup Guide

## What this workflow does
Every time you receive an email, n8n automatically:
1. Reads it from Gmail
2. Filters out newsletters and spam
3. Summarizes it using AI (OpenAI or Groq)
4. Posts the summary to a Slack channel

---

## Before you start — get these ready

| What you need | Where to get it |
|---|---|
| n8n account | https://n8n.io (free cloud) or run `npx n8n` locally |
| Gmail account | Any Gmail account |
| OpenAI API key | https://platform.openai.com/api-keys |
| OR Groq API key (free) | https://console.groq.com |
| Slack workspace | slack.com — must have permission to add apps |

---

## Step 1 — Open n8n and import the workflow

1. Log in to n8n
2. Click **"+ New workflow"**
3. Click the **"..."** menu (top right) → **"Import from file"**
4. Upload `email-to-slack.json` (OpenAI) or `email-to-slack-groq.json` (Groq — free tier)
5. The workflow will appear on your canvas with all 4 nodes ready

---

## Step 2 — Connect your Gmail

1. Click the **Gmail Trigger** node
2. Click **"Credential for Gmail OAuth2"** → **"Create new"**
3. A browser popup will appear — sign in with your Google account
4. Click **Allow** to grant n8n read access to Gmail
5. Click **"Test step"** — send yourself a test email first if your inbox is empty
6. You should see sample email data appear ✅

---

## Step 3 — Check the Filter node (no changes needed)

The filter is pre-configured to block:
- `noreply` addresses
- `no-reply` addresses
- `newsletter` senders
- `mailer-daemon` bounces

You can open the node and add more conditions if needed. Click **"Test step"** to verify.

---

## Step 4A — Connect OpenAI (if using email-to-slack.json)

1. Click the **AI Summarizer** node
2. Click **"Credential for OpenAI"** → **"Create new"**
3. Paste your OpenAI API key (starts with `sk-...`)
4. Click **"Test step"** — you should see a bullet-point summary appear ✅

The model is set to `gpt-4o-mini` — cheap and fast, about $0.0001 per email.

---

## Step 4B — Connect Groq (if using email-to-slack-groq.json)

1. Click the **Groq AI Summarizer** node
2. Click **"Credential"** → **"Create new"** → choose **HTTP Header Auth**
3. Set:
   - **Name**: `Authorization`
   - **Value**: `Bearer YOUR_GROQ_API_KEY_HERE`
4. Click **"Test step"** — you should see a summary in the response ✅

Groq is FREE on the free tier and uses `llama-3.1-8b-instant` (very fast).

---

## Step 5 — Connect Slack

1. Click the **Post to Slack** node
2. Click **"Credential for Slack OAuth2"** → **"Create new"**
3. A Slack popup will appear — choose your workspace and click **Allow**
4. In the **Channel** field, type your channel name e.g. `#email-digest`
   - Create this channel in Slack first if it doesn't exist
5. Click **"Test step"** — check your Slack channel for the message ✅

---

## Step 6 — Activate the workflow

1. Click **Save** (top right)
2. Toggle the **Active** switch (top right) to ON
3. Done! The workflow now runs every minute in the background 🎉

---

## Customizing the Slack message

Open the **Post to Slack** node and edit the Text field. Current format:

```
*📧 New Email Summary*

*From:* John Doe (john@example.com)
*Subject:* Meeting tomorrow at 3pm
*Received:* Mon, 12 Jun 2026

• The meeting is confirmed for tomorrow at 3pm
• You need to prepare the Q3 slides
• Reply by EOD to confirm attendance

——
```

---

## Troubleshooting

**Gmail trigger not picking up emails**
→ Make sure you sent a test email AFTER clicking "Test step"
→ Check that Gmail OAuth credential is authorized

**AI node returning an error**
→ Check your API key is correct and has credits
→ For Groq: make sure the header value starts with `Bearer `

**Slack message not appearing**
→ Check the channel name is spelled correctly (include the `#`)
→ Make sure the Slack bot has been added to that channel (type `/invite @n8n` in the channel)

**Workflow not running automatically**
→ Make sure the **Active** toggle is ON (green) in the top right

---

## Cost estimate

| Option | Cost per 100 emails |
|---|---|
| OpenAI gpt-4o-mini | ~$0.01 |
| Groq llama-3.1-8b-instant | Free |

---

## Files in this ZIP

```
n8n-email-slack/
├── workflow/
│   ├── email-to-slack.json          ← Import this for OpenAI version
│   └── email-to-slack-groq.json     ← Import this for Groq version (free)
├── docs/
│   └── SETUP_GUIDE.md               ← This file
└── scripts/
    └── test-groq.py                 ← Test your Groq API key locally
```
