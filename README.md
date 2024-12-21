**PRE-share data** is a tool that aims to assist resource aware design decisions during development of a self-serve data platform.

This tool consist of three main modules:

1. Pipeline generator and management dashboard
2. Reuse cong generator
3. Report dashboard


* **Pipeline generator and management dashboard**

This module will generate the pipelines, using kubeflow as platform, 
based on the user configuration file, upload the pipelines and start running an experiment. 

* **Reuse cong generator**

This module will auto generate an alternative recommended Configuration file,
that is generated automatically and based on reusing the common process across different pipelines defined in the user config file.

*  **Report dashboard**

This module provide bar and pie plots that shows the energy consumption of the pipelines and each of their process.


** Start working **

First you need to upload your config file in the YAML format in \data path. There is already a test sample for experiment.
