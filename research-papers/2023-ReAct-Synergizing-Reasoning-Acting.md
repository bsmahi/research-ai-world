# ReAct: Synergizing Reasoning and Acting in Language Models (2023)

**Authors**: Shunyu Yao et al. (Princeton & Google)

## 📝 Summary
ReAct explores the use of LLMs to generate both **reasoning traces** and **task-specific actions** in an interleaved manner. This allows the model to induce, track, and update action plans, and handle exceptions, essentially bridging the gap between reasoning (Chain-of-Thought) and acting (Action generation).

## 🔑 Key Concepts
- **Interleaved Reasoning & Acting**: The model produces a thought, then an action, then observes the result, effectively creating a feedback loop.
- **Improved Trustworthiness**: Reasoning traces allow humans to inspect the model's decision-making process.
- **Dynamic Planning**: The model can adjust its plan based on new information from the environment (e.g., search results).

## 🔗 Links
- [Paper (arXiv)](https://arxiv.org/abs/2210.03629)
- [Project Site](https://react-lm.github.io/)
