# Foundry Local

**Repository:** [https://github.com/microsoft/Foundry-Local](https://github.com/microsoft/Foundry-Local)

## Overview
Foundry Local brings the power of Azure AI Foundry to your local device without requiring an Azure subscription. It is designed to run generative AI models directly on local hardware with optimizations for ONNX Runtime and hardware acceleration (GPU/NPU).

## Key Features
- **Local Execution:** Run models locally without cloud dependencies.
- **Privacy:** Keep data processing on-device.
- **OpenAI Compatible API:** Integrate with applications using standard APIs.
- **Hardware Acceleration:** Supports Nvidia CUDA GPUs and Qualcomm NPUs.

## Quickstart
```bash
# Windows
winget install Microsoft.FoundryLocal

# macOS
brew install microsoft/foundrylocal/foundrylocal
```

## Usage
```bash
foundry model run phi-3.5-mini
```
