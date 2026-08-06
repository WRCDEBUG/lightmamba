
# Datasets

## LLVIP

LLVIP is a third-party public infrared-visible dataset. It is not redistributed in this package.

Expected structure under `DATA_ROOT/LLVIP`:

- `infrared/train`
- `visible/train`
- `infrared/test`
- `visible/test`
- `Annotations`

Revision manifests:

- train: `splits/llvip_revision_train.txt`, 10521 stems, SHA256 `0c94e87067626124947c1b28a6c6b43590a82f0241987f2a83cde7d76f2ef6e5`
- validation: `splits/llvip_revision_val.txt`, 1504 stems, SHA256 `1e594f2b95fc48d1ad2c633842b64853f455506e69f27b5ff56f099cb1b7fd66`
- validation groups: 03, 05, 15

Official test is evaluation-only and must not be used for model selection. Official test manifest SHA256: `45bc1e64dd837b33023fa9e65a62e2925fb53e29b1057daee82b9f309b94e64f`.

Official download URL: OFFICIAL_DOWNLOAD_URL_AUTHOR_CONFIRMATION_REQUIRED

## M3FD

M3FD is a third-party public infrared-visible dataset. It is not redistributed in this package.

Step 9A used 1050 exact-stem pairs for zero-shot fusion evaluation. Manifest SHA256: `55a33f7718b183a1666da7e69d21b8cbb37843321bbb11b94e6beb50d819d673`. No external detection AP was reported.

Official download URL: OFFICIAL_DOWNLOAD_URL_AUTHOR_CONFIRMATION_REQUIRED
