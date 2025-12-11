<p align="center">
  <img src="https://img.shields.io/badge/research--ai--world-000000?style=for-the-badge&logo=github&logoColor=white" />
</p>

<h2 align="center">🌍 Exploring the World of Artificial Intelligence 🤖</h2>

<p align="center">
  A curated collection of AI frameworks, research papers, tools, trends, and real-world use cases.
  <br/>
  Continuously updated to showcase how the world is rapidly moving toward AI adoption.
</p>

<br/>

<p align="center">
  <img src="https://img.shields.io/badge/Artificial%20Intelligence-Research-blueviolet?style=flat-square" />
  <img src="https://img.shields.io/badge/Machine%20Learning-Frameworks-orange?style=flat-square" />
  <img src="https://img.shields.io/badge/Deep%20Learning-Neural%20Networks-brightgreen?style=flat-square" />
  <img src="https://img.shields.io/badge/Research-Papers-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/AI%20Use%20Cases-Real%20World-yellow?style=flat-square" />
  <img src="https://img.shields.io/badge/AI%20Tools-Ecosystem-9cf?style=flat-square" />
</p>

<hr/>

## 📘 Overview

This repository is a **central hub for everything AI**. It serves as both a knowledge base and a practical playground for developers and researchers.

**What you will find here:**
- **Frameworks Deep Dives**: Detailed overviews of cutting-edge agent frameworks.
- **Hands-on Examples**: Runnable code snippets with Docker support.
- **Research Summaries**: TL;DRs of seminal papers that shaped the industry.
- **Tooling Ecosystem**: Curated lists of observability and database tools.

---

## 📁 Project Structure

```markdown
research-ai-world/
├── examples/                       # Python & Docker examples for Agent frameworks
│   └── python/                     # Code for CrewAI, AutoGen, Google ADK, Strands
├── frameworks/                     # Documentation hub for AI frameworks
│   ├── crewai/                     # Role-playing agents
│   ├── microsoft-autogen/          # Multi-agent conversation
│   ├── google-adk/                 # Agent Development Kit
│   ├── strands-agents/             # Model-driven planning
│   └── springai/                   # AI for Java developers
├── research-papers/                # Summaries of key papers (Attention, ReAct, Magentic-One)
├── tools/                          # Ecosystem tools (Observability, Vector DBs)
├── usecases/                       # Real-world AI use cases
├── resources/                      # Learning resources, courses, and cheatsheets
└── README.md                       # Project documentation
```

---

## 🚀 Frameworks & Examples

We explore various frameworks to understand different paradigms of building AI agents. Checked folders contain details and examples.

| Framework | Description | Example Code |
| :--- | :--- | :--- |
| **CrewAI** | Orchestrate role-playing autonomous agents. | [View Code](examples/python/crewai/main.py) |
| **Microsoft AutoGen** | Framework for conversational agents. | [View Code](examples/python/autogen/main.py) |
| **Google ADK** | Build agents optimized for Vertex AI/Gemini. | [View Code](examples/python/google-adk/main.py) |
| **Strands Agents** | Model-driven approach to agent planning. | [View Code](examples/python/strands-agents/main.py) |
| **Spring AI** | Portable AI API for Java applications. | *(Docs Only)* |
| **Embabel** | Goal-oriented agents for the JVM. | *(Docs Only)* |

---

## 🧠 Research Lab

Understanding the "Why" behind the "How". We maintain summaries of seminal research papers in `research-papers/`.

- **Foundation**: *Attention Is All You Need (2017)*
- **Reasoning**: *ReAct: Synergizing Reasoning and Acting (2023)*
- **Multi-Agent**: *Magentic-One (2024)*, *Mixture-of-Agents (2024)*
- **RAG**: *Retrieval-Augmented Generation Survey (2024)*

---

## 🛠️ Tools of the Trade

Building production AI requires more than just models. Check `tools/` for curated lists of:
- **Observability**: LangSmith, Arize Phoenix, Grafana.
- **Vector Databases**: Pinecone, Weaviate, Qdrant.
- **Coding Assistants**: GitHub Copilot, Cursor.

## 📚 Resources

Never stop learning. Check `resources/` for:
- Free courses from DeepLearning.AI and Hugging Face.
- Cheatsheets for LangChain and Prompt Engineering.

---

## 🤝 Contributing
Pull requests are welcome! You can contribute by adding new use cases, research notes, or improving examples.

1. **Fork and Clone**. Fork the `bsmahi/research-ai-world` repository on GitHub and clone your fork locally:
    ```shell
    git clone https://github.com/<your-username>/research-ai-world.git
    cd research-ai-world
    ```
2. **Implement Changes**. Make your code changes. Follow the [Code Style](#code-style) guidelines.
3. **Update Documentation**. If necessary, update documentation in the `README.md` files
4. **Build and Test Locally**. Ensure everything builds and all tests pass
5. **Commit Changes**. Commit your work using descriptive messages that follow the [Commit Messages](#commit-messages) format. Crucially, ensure your commits are signed off (see [Signing Commits](#signing-commits)).
    ```shell
    git add .
    git commit -s -m "feat(core): Implement the new feature"
    ```
> [!IMPORTANT]

6. **Keep Branch Updated**. Before pushing, and periodically during development, update your branch with the latest changes from the upstream `main` branch using rebase (NEVER merge):
    ```shell
    # Add upstream remote if you haven't already
    git remote add upstream https://github.com/arconia-io/arconia.git

    # Fetch latest changes and rebase your branch
    git fetch upstream
    git rebase upstream/main
    # Resolve any conflicts if they occur
    ```
7. **Push to Your Fork**. Push your branch to your fork. Use `--force-with-lease` if you rebased or amended commits:
    ```shell
    git push origin master --force-with-lease
    ```   


### Code Style

* The project uses [.editorconfig](/.editorconfig) to define basic code formatting. Please ensure your editor respects this file.
* Use explicit imports; avoid wildcard (`*`) imports.
* Follow the existing sorting order when adding items to lists (usually alphabetical).

### Commit Messages

We follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification for PR titles and commit messages. This aids automated releases and improves history readability.

Format:
```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

* **Types**: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `build`, `ci`, `chore`, `revert`, `deps`.
* **Scopes** (optional, relate to project modules): `core`, `dev`, `k8s`, `multitenancy`, `otel`. Do not include a scope if the change doesn't relate to one of these modules.
* **Description**: Use present tense ("Add feature", not "Added feature") and imperative mood ("Move cursor", not "Moves cursor").
* **Breaking Changes**: Indicate breaking changes with `BREAKING CHANGE:` in the footer or by appending `!` after the type/scope (e.g., `feat(core)!:`).

Example: `fix(dev): Correct handling of container startup timeout`

The Pull Request title *must* also follow this convention.

### Signing Commits

All commits contributed to Arconia must be **signed-off**, attesting to the [Developer Certificate of Origin (DCO)](#developer-certificate-of-origin-dco-sign-off).

Commits lacking sign-off will block merging.

#### Developer Certificate of Origin (DCO) Sign-off

The DCO certifies you have the right to submit your contribution.

The easiest way to sign-off a commit is using the `-s` flag:

```shell
git commit -s -m "Your commit message"
```

To add a sign-off to your *last* commit if you forgot:

```shell
git commit --amend -s --no-edit
```

For older commits, use interactive rebase (`git rebase -i`).

## ⭐ Support
If you find this project useful:
- ⭐ Star the repo
- 🍴 Fork it
- 🗣️ Submit suggestions

## Code of Conduct

All participants in the Research AI World community are expected to adhere to our minimum code of conduct. Please understand the expected standards of behavior. Treat everyone with respect and kindness.
