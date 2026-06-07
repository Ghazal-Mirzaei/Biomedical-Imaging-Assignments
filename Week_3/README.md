# Week 03 — Image Filtering

## Overview
This notebook explores spatial filtering techniques applied to medical images,
covering smoothing filters and noise removal strategies.

## Tasks

| Task | Method | Description |
|------|--------|-------------|
| 1 | Box Filter | Custom 5×5 normalized kernel via `cv2.filter2D` |
| 2 | Gaussian Filter | Blur comparison across 3×3, 7×7, and 15×15 kernels |
| 3 | Median Filter | Salt & pepper noise removal on additive and multiplicative noise |

## Images Used
- `filter_gaussian.png` — Abdominal CT scan
- `filter_specklenoise.png` — Image with speckle noise
- `saltandpepper_add.png` — Chest X-ray with additive salt & pepper noise
- `saltandpepper_multiply.png` — Chest X-ray with multiplicative salt & pepper noise

## Key Findings
- Larger Gaussian kernels produce progressively stronger blur, losing fine detail
- The median filter effectively removes multiplicative salt & pepper noise
- For very high noise density (additive), a single median pass is insufficient —
  the noise pixels outnumber signal pixels in each neighborhood
- Unlike box/Gaussian filters, the median filter preserves edges while removing noise
