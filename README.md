

<div align="center">
<img width="300" height="213" alt="image" src="https://github.com/user-attachments/assets/305289a6-5dca-4a7b-aefc-9f1f31c1756a" />

# MAST4Science
[![arXiv](https://img.shields.io/badge/arXiv-TODO.svg)](TODO)
![python](https://img.shields.io/badge/python-3.12%2B-blue)
[![license](https://img.shields.io/badge/License-MIT-green.svg?labelColor=gray)](https://github.com/WUR-AI/aether/blob/main/LICENSE) <br>
[![PRs](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/com3dian/multi_agent_system_template/pulls)
[![Issues](https://img.shields.io/github/issues/com3dian/multi_agent_system_template)](https://github.com/com3dian/multi_agent_system_template/issues)
![GitHub Tag](https://img.shields.io/github/v/tag/com3dian/multi_agent_system_template)
[![contributors](https://img.shields.io/github/contributors/com3dian/multi_agent_system_template.svg)](https://github.com/com3dian/multi_agent_system_template/graphs/contributors)

</div>
<br>

This project is under rapid development, and the documentation is not yet mature. For now, implementation guidance can be found in the docstrings and comments in the source code.

## Development

This project uses [Black](https://black.readthedocs.io/) as its mandatory Python
formatter. The exact Black version is pinned so local checks and CI produce the
same result.

```bash
python -m pip install -r requirements-dev.txt
pre-commit install
```

Format maintained Python code with:

```bash
black .
```

Run the same strict check enforced by commits and CI with:

```bash
black --check --diff .
```

Archived code under `legacy/` is intentionally excluded.
