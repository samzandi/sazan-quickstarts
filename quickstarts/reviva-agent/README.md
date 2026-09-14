# ReViva Agent Quickstart

A provider-neutral, security-first planning quickstart for photo restoration.

This MVP does **not** process image pixels. It works only with bounded local mock metadata and produces deterministic restoration plans.

## Core invariant

Identity preservation is mandatory. Requests that could replace or alter a person's identity are rejected fail-closed.

## Supported operations

- `denoise`
- `deblur`
- `face_restore`
- `upscale`

## Explicitly blocked

- face replacement
- identity changes
- synthetic faces
- adding synthetic facial features
- unknown restoration operations

## Safety boundaries

No external network access, shell execution, credential handling, arbitrary filesystem access, model download, cloud upload, or real image processing is performed.

This quickstart is not production-ready. A production restoration system would still require validated model pipelines, identity-similarity measurement, privacy controls, secure storage, failure handling, observability, and real image-quality evaluation.

## Run

```bash
cd quickstarts/reviva-agent
python app.py
python -m unittest discover -s tests -p 'test_*.py'
```
