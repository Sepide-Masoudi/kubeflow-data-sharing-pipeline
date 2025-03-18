# PRE-share Data Tool

**PRE-share Data** is a tool designed to assist in making resource-aware design decisions during the development of a self-serve data platform. It provides a comprehensive suite of modules to generate, manage, and analyze data pipelines, with a focus on reusability and energy efficiency.

## Overview

The tool consists of three main modules:

1. **Pipeline Generator and Management Dashboard**
2. **Reuse Configuration Generator**
3. **Report Dashboard**

---

### 1. Pipeline Generator and Management Dashboard

This module generates pipelines using **Kubeflow** as the platform, based on a user-provided configuration file. It also provides a dashboard to manage and monitor the pipelines.

- **KubeflowPipelineGenerator**: Generates pipelines based on the configuration file.
- **Management_Dashboard**: Runs experiments and checks the status of pipelines.

---

### 2. Reuse Configuration Generator

This module automatically generates an alternative recommended configuration file. It identifies and reuses common processes across different pipelines defined in the user's configuration file, optimizing resource usage.

---

### 3. Report Dashboard

This module provides visualizations (bar and pie plots) to show the energy consumption of pipelines and their individual processes, helping users make informed decisions about resource allocation.

---

## Getting Started

### Prerequisites

- Ensure you have a configuration file in **YAML** format ready. A sample configuration file (`shipments_pipeline_config`) is provided in the `\data` path for testing purposes.

### Steps to Run the Tool

1. **Upload Configuration File**:
   - Place your configuration file in the `\data` directory.
   - Update the path in the `KubeflowPipelineGenerator` to point to your configuration file.
   - If using a custom dataset, update the URL to your dataset.

2. **Generate Pipelines**:
   - Run the `main` method in the `KubeflowPipelineGenerator` to compile the pipelines.

3. **Run Experiments**:
   - Go to the `Management_Dashboard` and run a round of experiments.
   - Use the provided function to check the status of your pipelines. Proceed once the status changes to **"SUCCESS"**.

4. **Generate Reports**:
   - Run the `main` function in the `Report_Dashboard` to generate energy consumption reports for your pipelines.

5. **Reuse Configuration**:
   - Run the code in the `ReuseConfigGenerator` to generate an alternative configuration file that optimizes pipeline reuse.
   - Re-run your pipelines with the new configuration and measure the updated metrics.

---

## Extending the Tool

You can extend the tool by adding support for additional operations as pipeline stages. To do this, add your custom functions to the `stages` function definitions cell in the `KubeflowPipelineGenerator`.

---

## Contributing

We welcome contributions! If you'd like to contribute, please fork the repository and submit a pull request with your changes.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

For any questions or feedback, please reach out to sepideh.masoudi@tu-berlin.de or open an issue in the repository.

---
