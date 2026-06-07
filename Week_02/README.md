# Week 02 — Contrast Enhancement

## Overview
This notebook explores contrast and brightness manipulation techniques
applied to medical images (chest X-ray and CT scan).

## Tasks

| Task | Method | Description |
|------|--------|-------------|
| 1 | Brightness & Contrast | `convertScaleAbs` and `addWeighted` to reveal vessel structures |
| 2 | Contrast Stretching | Linear remapping of pixel range to [0, 255] |
| 3 | Histogram Equalization | Global equalization on X-ray and CT images |
| 4 | CLAHE | Adaptive local contrast enhancement |
| 5 | Thresholding | Otsu's method for lung segmentation |
| 6 | Histogram Matching | Matching source histogram to CLAHE reference |

## Images Used
- `contrast_stretching.png` — Chest X-ray
- `CONTRAST_1_CT.tif` — CT scan (float64, Hounsfield Units)
- `best_contrast.png` — CLAHE-enhanced output

## Key Findings
- Contrast stretching has no effect when the image already spans [0, 255]
- Global histogram equalization can over-enhance uniform regions
- CLAHE produces more natural results by working on local tiles
- Median-based thresholding (Otsu) outperforms manual threshold selection
