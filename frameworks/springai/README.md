# Spring AI

<div align="center">
  <img src="https://docs.spring.io/spring-ai/reference/_images/spring_ai_logo_with_text.svg" alt="Spring AI Logo" width="300"/>
</div>

**Spring AI** is an application framework for AI engineering. It provides a portable API across AI providers for chat, text-to-image, and embedding models. It integrates AI concepts into the familiar Spring ecosystem.

## 🚀 Key Features
- **Portable API**: Consistent API for interacting with various AI models (OpenAI, Azure, Bedrock, Ollama, etc.).
- **Prompt Engineering**: Support for templated prompts and standardizing interactions.
- **Function Calling**: Map Java functions to LLM tools seamlessly.
- **ETL Pipeline**: Document readers and vector store support for RAG applications.

## 📦 Installation
Add the Spring AI BOM and dependencies to your `pom.xml` (Maven):

```xml
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>org.springframework.ai</groupId>
            <artifactId>spring-ai-bom</artifactId>
            <version>1.0.0-SNAPSHOT</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
```

## 📚 Resources
- **GitHub Repository**: [spring-projects/spring-ai](https://github.com/spring-projects/spring-ai)
- **Documentation**: [docs.spring.io/spring-ai](https://docs.spring.io/spring-ai/reference/)
- **Awesome Spring AI**: [spring-ai-community/awesome-spring-ai](https://github.com/spring-ai-community/awesome-spring-ai)
- **ByteSized AI**: [www.bytesizedai.dev](https://www.bytesizedai.dev)