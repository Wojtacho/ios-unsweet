# SM-A510F port: engineering log
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
## 2026-11-10: probe run 1 (commit 9217ddc, Actions run 42782171816)
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Device: SM-A510F, firmware A510FXXS8CSF3 (Android 7.0), hw_rev 4
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
(running DT reports `model_info-hw_rev` 3, matched by the 3-7 dt.img entry).
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Flashed `a510f-probe-recovery.tar` to RECOVERY with Odin 3.13.3 (Auto Reboot
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
off). First attempt was lost: Android booted before recovery and the stock
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
`install-recovery` restored Samsung recovery. Second attempt, going straight
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
from download mode to recovery (Vol Down+Home+Power, then swap Vol Down for
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Vol Up), ran the probe and drew all 13 rows.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Decoded from a photo of the screen:
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
| Row | Value | Meaning |
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
|---|---|---|
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
| 0 alive | `0xFFFFFFFF` | S-Boot runs our arm64 Image; display works |
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
| 1 EL | `0x00000001` | entered at **EL1** (no EL2 access) |
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
| 2 PSCI_VERSION | `0xFFFFFFFF` | NOT_SUPPORTED, no fault: PSCI 0.1-style firmware (IDs from DT) |
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
| 3 CPU_ON | `0x00000000` | SUCCESS with 0xC4000003 |
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
| 4 2nd core | `0xC0DE0001` | second A53 came up at EL1 and ran our code |
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
| 5 ID_AA64ISAR0 | `0x00011120` | AES+PMULL, SHA1, SHA2, CRC32; **Atomic = 0 (no LSE)** |
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
| 6 ID_AA64MMFR0 | `0x00001122` | 40-bit PA, 16-bit ASID; **TGran16 = 0 (no 16 KB pages)**; 4K and 64K OK |
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
| 7 MIDR | `0x410FD033` | Cortex-A53 r0p3 |
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
| 8 exceptions | `0x00000000` | none taken |
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
| 9 load address | `0x40205000` (photo read, low confidence on bits 15:12) | where S-Boot placed the Image |
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
| 10 DTB | `0x48000000` | x0 at entry |
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
| 11 framebuffer | `0x67000000` | DECON window 0 buffer left by S-Boot |
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
| 12 display | win 0, fmt 0 (ARGB8888), TRIGCON `0x0088` | HW (TE) trigger mode; unmasking HWTRIGMASK refreshes the panel |
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Observations vs. guesses:
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
- Observed: 64-bit boot, EL1, SMP bring-up via PSCI CPU_ON, framebuffer
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  console via S-Boot's DECON setup. These are enough for an XNU bring-up shim.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
- Observed: no LSE atomics, no 16 KB granule. Hardware facts, not fixable.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
- Guess: PSCI SYSTEM_OFF is likely unsupported too (PSCI_VERSION is).
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  Power-off timing not yet reported.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Power-off: the phone switched itself off ~60 s after the rows appeared, so
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
the probe ran to the end (PSCI SYSTEM_OFF or the PS_HOLD fallback; not
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
distinguished).
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
## 2026-11-10: iOS 16 instruction scan (run 42790485292, commit 776368e)
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
`a510f-isa-scan` workflow, `a510f/tools/dsc_isa_scan.py`: iPhone X iOS
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
16.7.16 (20H392) main dyld shared cache from the SystemOS cryptex
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
(`087-86593-047.dmg`), code sections only, exact encodings.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
| | count |
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
|---|---|
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
| images scanned | 2647 |
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
| instructions | 387,147,500 |
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
| LL/SC exclusives (ARMv8.0 atomics) | 823,085 |
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
| **LSE atomics** | **990** in 21 images (CAS 346, CASP 15, LD*/SWP 629) |
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
| FP16 arithmetic | 1530 (1417 in libBNNS, 74 in ActionKit) |
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
| RDMA (SQRDMLAH/SH) | 50 (33 in ActionKit) |
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
| LDAPR | 1 |
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
| DC CVAP | 0 |
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
LSE by image: libdispatch 697, libsystem_pthread 86, libsystem_platform 81,
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
ActionKit 73, libsystem_malloc 20, the rest 1-6 each (libsystem_m,
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
libSparse, MediaToolbox, AudioCodecs, corecrypto, MobileGestalt, dyld, ...).
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Reading:
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
- The compiler baseline for this userland is ARMv8.0: libobjc, libswiftCore,
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  Foundation, CoreFoundation, UIKitCore, libc++ and JavaScriptCore have
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  **zero** LSE and use LL/SC throughout.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
- LSE sits only in the hand-tuned atomics of libdispatch / pthread /
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  platform / malloc, which also carry LL/SC paths. Guess (to verify in xnu
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  `cpu_capabilities.h` and libplatform): these pick LSE at run time from a
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  commpage capability bit the kernel sets from ID_AA64ISAR0. On the A53 that
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  bit stays clear and the LL/SC paths run, at no cost.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
- Whatever still executes LSE/FP16/RDMA can be trapped (undefined
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  instruction) and emulated in the kernel. Only niche code (Shortcuts'
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  ActionKit, BNNS neural-net kernels) has more than a handful of sites.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
- Conclusion: **atomics are not a blocker.** The 16 KB page granule is now
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  the main open problem.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
## 2026-11-10: 4 KB pages in xnu-8796 (source study, xnu-8796.141.3)
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Finding: **xnu-8796 still carries a 4 KB-page arm64 configuration**, and it
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
is for a Cortex-A53: `MACHINE_CONFIG=BCM2837` (Raspberry Pi 3).
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
- `makedefs/MakeInc.def`: `SUPPORTED_ARM64_MACHINE_CONFIGS = BCM2837 T6000
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  T8101 T8103 VMAPPLE`; `MACHINE_FLAGS_ARM64_BCM2837 = -DARM64_BOARD_CONFIG_BCM2837`
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  (no `-mcpu`, i.e. plain ARMv8.0).
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
- `pexpert/pexpert/arm64/BCM2837.h` defines `__ARM_ARCH__ 8`,
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  `__ARM_VMSA__ 8`, `__ARM64_PMAP_SUBPAGE_L1__ 1`, `NO_MONITOR`, and **no
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  `__ARM_16K_PG__`** (H13.h and VMAPPLE.h define it). sweet's patch 0004
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  defines it for SWEET.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
- Without `__ARM_16K_PG__`: `ARM_PGSHIFT 12` (proc_reg.h) and
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  `PAGE_SHIFT_CONST 12` (mach/arm/vm_param.h), so the VM, pmap and user
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  `vm_page_size` are all 4 KB. The pmap, TLB and proc_reg code keep full
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  `#else` 4 KB branches (4K L0-L3 table geometry).
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
- Shared cache sliding is page-size independent: `PAGE_SIZE_FOR_SR_SLIDE`
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  is 4096 everywhere (vm_shared_region.h), so the iOS 16 cache's slide info
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  is usable.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Atomics, confirmed in the kernel source:
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
- `osfmk/arm/commpage/commpage.c` sets `kHasFeatLSE` (= `kHasARMv81Atomics`)
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  only when `ID_AA64ISAR0_EL1.Atomic >= 8.1`; RDM and FP16 bits likewise come
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  from the ID registers. On the A53 they stay clear, so libdispatch,
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  pthread, platform and malloc take their LL/SC paths.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
- The only explicit LSE in the kernel (`casa` in
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  `hw_lck_ticket_reserve_orig_allow_invalid`, machine_routines_asm.s) is
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  under `#if defined(__ARM_ARCH_8_2__)`. sweet builds with
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  `-march=armv8.2-a+crypto`; an A510F config must use `-march=armv8-a+crc+crypto`
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  so neither this nor compiler-generated atomics use LSE.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
sweet patches that assume 16 KB (from grepping `xnu/patches`):
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
- 0004 (machine config: defines `__ARM_16K_PG__`): new A510F config instead.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
- 0010 (early framebuffer block mapping assumes the 16K bootstrap table
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  layout, `+ 2*PGBYTES`, 32 MB L2 block): rewrite for 4K (2 MB L2 blocks).
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
- 0011 (physmap padding) is written in `ARM_TT_*` terms: should follow.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
- Other hits (0028 `DMA_BOUNCE 0x4000`, 0046, 0058, 0060, 0073) are buffer
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  or MMIO sizes, not page-size assumptions.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Risks still open (cannot be settled from source):
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
- iOS 16 userland never shipped on 4 KB-page hardware (the last 4 KB arm64
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  iOS was iOS 12 on A7/A8). Code that reads `vm_page_size` adapts; anything
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  hard-coding 16 KB will show up only at run time.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
- Whether the BCM2837 config still builds cleanly with this toolchain.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  Apple's open-source releases do list it; nothing here shows it booting.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Verdict: 16 KB pages are **not a blocker in principle**. The kernel side is a
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
supported configuration; the work is a new A510F machine config modelled on
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
BCM2837 plus porting sweet's SWEET-specific patches to it.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
## 2026-11-10: first 4 KB / Cortex-A53 kernel build (a510f-xnu run 42803068442, commit 7a9c842)
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Result: `kernel.development.sweet`, 17,203,280 bytes, Mach-O arm64,
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
sha256 d355129c9203d687...; the Linux `isa-check` job found **no
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
A53-incompatible instructions** in 2,290,622 instructions (2,271 LL/SC
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
exclusives; the one LSE-shaped word is the SHA-256 `K256` table in
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
`__hib_text`, data).
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
How it is built (`.github/workflows/a510f-xnu.yml`):
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
- sweet's 77 patches + `a510f/xnu/make-a510f-variant.sh` on the copied 0004:
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  no `__ARM_16K_PG__`, `__ARM64_PMAP_SUBPAGE_L1__` instead of
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  `__ARM_PAN_AVAILABLE__`, `-mcpu=cortex-a53`. Machine config name stays
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  SWEET, so the board code is still sweet's (GICv3, UFS, Goodix...).
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
- `a510f/xnu/patches/0100`: 4K commpage nesting static_assert skipped on
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  macOS-platform builds (the 1GB nesting region is reserved by the VM, as
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  the 16K branch documents). The only compile error of the 4 KB build.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
- `a510f/xnu/patches/0101`: commpage PFZ FIFO trylocks (user-visible
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  OSAtomicFifoEnqueue/Dequeue) use LDAXR/STXR when `__ARM_FEATURE_ATOMICS`
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  is off; they were unconditional `casa`.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
- `a510f/xnu/patch-dxb-build.sh`: libfirehose_kernel is built by xcodebuild
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  outside xnu's makefiles; build only its arm64 slice with
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  `-mcpu=cortex-a53`.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
- Runner: `macos-15-intel`. macos-14 is retired; arm64 macOS runners
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  repeatedly never picked the job up. Xcode 16.0 builds xnu-8796 here
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  (sweet chose macos-14 for Xcode 15's iig; not needed so far).
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Lessons (observed, with run ids in git log):
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
- `-march=armv8-a` alone left Apple clang's default CPU (apple-m1) in
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  charge: 875 LSE + 209 LDAPR in the kernel. Use `-mcpu`.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
- Run logs need a GitHub login; workflows publish errors as annotations,
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  readable via the check-runs API or the run page.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
## 2026-11-10: first xnu boot on the A510F (a510f-xnu run 42807157271, commit ab07160)
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Image: `a510f-xnu-recovery.tar` (shim 77,824 B + SWEETXNU payload
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
16,493,360 B), flashed to RECOVERY with Odin, booted straight from download
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
mode into recovery. Kernel cmdline `debug=0xc serial=3 cpus=1 keepsyms=1
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
-enable_kprintf_spam`.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Observed (photo):
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
- Shim red screen: payload found, `VIRT FFFFFFF006000000`, `ENTRY
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  FFFFFFF007428488`, `SEGS n=0A end=724AC000`, `BOOTARG pa=724B0000
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  top=724B4000`, `JUMP 71428488`. The DECON/CPU1 lines had scrolled away.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
- Stage-0 white band, then green stage bands: xnu's first instruction ran.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
- `SWEET EARLY 1` .. `7`: arm_init with the 4K MMU on, PE_init_platform
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  (ADT), ml_parse_cpu_topology (8 A53 MPIDRs), cpu_bootstrap,
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  kernel_startup_bootstrap, cpu_init, entering arm_vm_init.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
- The display kept updating after the jump: the CPU1 DECON refresher works.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
- `SWEET EARLY PANIC: arm_vm_init.c:1843 Assertion failed: (l1 &
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  (ARM_TTE_VALID | ARM_TTE_TYPE_MASK)) == (ARM_TTE_VALID |
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  ARM_TTE_TYPE_TABLE)` in sweet_early_map_final: without ARM_LARGE_MEMORY
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  no L2 table exists at VM_MIN_KERNEL_ADDRESS for the early-console alias.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Fix (commit 270f478, patch 0102): allocate that L2 table with alloc_ptpage
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
when the L1 entry is empty; clear the alias blocks when the early console is
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
disabled after kprintf startup.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
## 2026-11-10: second boot (a510f-xnu run 42809529936, commit 270f478)
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Observed (photo): the early console ran through arm_vm_init and was
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
replaced by the normal framebuffer console, i.e. stages 8-20 passed:
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
`kprintf initialized`, `Serial mode specified: 00000003`,
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
`initialize_screen: b=67000000, w=00000438, h=00000780, r=000010E0, d=0`,
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
`pe_arm_init_interrupts`, `pe_arm_map_interrupt_controller: failed to find
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
the interrupt-controller` (message only), `pe_arm_init_debug: failed to find
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
cpu-debug-interface`, `SWEET GIC: virtual timer INTID 27`, then
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
`panic(cpu 0 caller 0xfffffff007b19748): find_gicr_pe_base: cannot find GICR
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
base for core 0 @pe_fiq.c:73` and nested panics ending in "Nested panic
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
stall. Stage 2 bailout" (spins; screen stays on).
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Also observed: after this image ran, Vol Down + Power and the download-mode
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
"cancel" restart both came back into recovery (our image), not Android. Way
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
out used: download mode (Vol Down + Home + Power, then Vol Up), charging.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Fix (commit bc2409f, patch 0103): GIC-400 (GICv2) through GICD/GICC MMIO
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
(per-CPU init, IRQ ack/EOI, SGIs via GICD_SGIR) and power-off 60 s after a
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
panic (PSCI SYSTEM_OFF, then PS_HOLD).
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
## 2026-11-10: third boot (a510f-xnu run 42814550274, commit bc2409f)
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Observed (photo), new after the GIC: `SWEET GIC: GICv2 cpu 0 ctlr 0x1 en0
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
0x800feff` (GICC Grp1 enabled; SGIs 0-15 and INTID 27 enabled), `Darwin
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Kernel Version 22.6.0 ... xnu-8796.141.3`, `pmap_startup() init/release time:
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
42065 microsec`, `vm_page_bootstrap: 243454 free pages, 13314 wired pages`
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
(4K pages: ~950MB managed), `VM bootstrap: 73 maps, 153 entries and 128 holes
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
available`, `Maximum number of VM swap files: 100`, then `panic: kmem_range_init:
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
vm_map_locate_space failing for claim kmem_data_range @vm_kern.c:3645`.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Also printed: "iBoot didn't extract panic log from previous session crash".
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
**The 60 s auto power-off worked** (user report).
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Cause: zalloc.c sizes the zone map for XNU_PLATFORM_MacOSX (128GB VA,
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
32GB max); without ARM_LARGE_MEMORY the kernel VA is the iOS layout
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
(~112GB), so the claims cannot fit.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Fix (patch 0104): iOS zone sizes (24GB VA, 8GB max) for arm64 builds without
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
ARM_LARGE_MEMORY; kmem_range_init prints every claim's size before such a
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
panic.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
## 2026-11-10: fourth boot (a510f-xnu run 42820603306, commit d13ae1c)
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Observed (photo): the iOS zone sizes fixed kmem_range_init. Full panic
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
report on screen: zone map 0xfffffff07a000000-0xfffffff67a000000 (24GB) with
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
PGZ/VM/RO/GEN0-3/DATA ranges, metadata and bitmaps; panicked task pid 0,
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
thread tid 101 with a 16-frame backtrace; stackshot succeeded; "Kernel text
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
base: 0xfffffff007004000". Panic: `recount.c:964 Assertion failed:
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
(snap->rsn_time_mach & RCT_PR_IDLING) == 0`. `mach_absolute_time:
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
0xbd9316b97414c5be`: S-Boot leaves CNTVCT_EL0 near 2^63, and recount keeps
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
its idle flag in bit 63 of mach time.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Fix (patch 0105): right after cpu_data_init in arm_init, set
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
rtclock_base_abstime = -CNTVCT (copied to cpu_base_timebase by
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
cpu_timebase_init and published in the commpage), so mach time starts near 0.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
The decrementer uses CNTV_TVAL (relative), so the offset does not affect
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
timer programming.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
## 2026-11-10: fifth boot (a510f-xnu run 42828923119, commit ccc5716): no panic, IOKit up
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Observed (two photos): zone_init with all submaps (VM/RO/GEN0-3 3686M each,
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
DATA 4914M, metadata 96M), `VM bootstrap done: 61 maps, 112 entries and 117
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
holes left`, `IOKit IOMD setownership ENABLED`, ATM, log queues, Firehose,
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
OSLog, `Telemetry: Sampling all tasks once per 1 second`, `Scheduler: Default
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
of clutch`, timeslicing quantum 10000 us, mig/BANK/IPC_PTHREAD_PRIORITY,
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
panic_trace, kdp_core, `Initializing serial KDP`, `iBoot version: sweet-shim`,
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
`ulock_initialize: thread_max=2560`, SWEET PRNG (HMAC-SHA256), SWEET pthread
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
(libpthread-514.100.2), SWEET AMFI (built-in, XML entitlements), vnguard
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
policy, `SWEET: trust caches unavailable`, keepsyms, `SWEET: starting
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
device-tree platform expert` / `platform expert registered`, `SWEET FB:
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
AppleCLCD 1080x1920 stride 4320 at 0x67000000, default surface 1, presented
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
as 1125x2436`, SWEET AKS, WDT, SURF (IOCoreSurfaceRoot), HID buttons, HID
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
touch, `SWEET BATTERY: static fallback, 100% 4200mV`. A boot progress bar is
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
drawn mid-screen. No panic seen (so no auto power-off).
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Reading: the GICv2 timer interrupt and the rebased timebase work (the
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
scheduler and 1 s telemetry run). Expected next: waiting for the root
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
device (no storage driver for the eMMC, no iOS root on the phone yet).
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
## 2026-11-10: sixth/seventh boot: kernel waits for the root device
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Sixth boot (repack run 42834299958, boot-args `... sweetkeys=0 sweettouch=0
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
sweetusb=0`): same silent stop after `SWEET FB`, and the keys/touch
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
"disabled" lines never printed: boot stopped before those drivers. Cause:
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
SweetCPU is matched with IONameMatch 'qcom,kryo470'; the A510F ADT CPU
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
nodes only said arm,cortex-a53, so CPU 0 never registered with IOKit.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Seventh boot (repack run 42836001379, commit 1e8a69d: CPU nodes compatible
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
'arm,cortex-a53', 'qcom,kryo470', 'ARM,v8'; kernel from a510f-xnu run
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
42828923119). Observed (two photos):
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
- `SWEET CPU: requested=1 selected=1 (limit=8)`, `cpu_start() cpu: 0`,
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  `SWEET CPU: cpu=0 entered initCPU mpidr=0x0 EL1 IRQs=1`, `... came alive;
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  SGI1 OK`, `SWEET CPU: 1/1 CPUs initialized, SGI1 verified` (GICv2 SGI
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  delivery works), `ml_processor_register ... cpu_number 0 is type 0`.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
- BSD: copyright banner, `MAC Framework successfully initialized`, buffer
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  headers, ktriage, SWEET AMFI policy, SWEET permissive Sandbox, `SWEET HFS:
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  hfs-627.100.6 registered`, mcache/mbinit (64 MB pool), DLIL SUM16 self-test
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  PASSED, Skywalk self-tests all PASSED, lo0/gif0/stf0 attached.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
- Last: `Waiting on <dict ID="0"><key>IOProviderClass</key><string
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  ID="1">IOMedia</string><key>Content</key><string
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  ID="2">Apple_HFS</string></dict>`: IOFindBSDRoot waiting for an HFS root.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
**Milestone: the A510F completes XNU kernel startup up to the root mount.**
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Next: a block device for the root (eMMC host driver, or a RAM-disk root for a
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
first userland test) and an iOS root filesystem image.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
## 2026-11-10: eighth boot: user space PID 1 on the A510F
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Image: a510f-repack run 42837467623 (commit 0641695): kernel from a510f-xnu
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
run 42828923119, boot-args `debug=0xc serial=3 cpus=1 keepsyms=1
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
-enable_kprintf_spam sweetkeys=0 sweettouch=0 sweetusb=0 rd=md0`, RAM disk =
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
sweet's static init (`tools/sweet-init.S` built with Ubuntu clang
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
`-target arm64-apple-ios16.0`, wrapped by `tools/mkinit.py`), passed via
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
`a510f/build.sh xnu KERNEL CMDLINE ROOTFS` -> `mkpayload.py --ramdisk`.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Observed (two photos): `"RAMDisk" not a kext`, `Added memory device
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
md0/rmd0 (01000000/12000000) at FFFFFFF0084AC000 0 for 0000000000008000`,
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
`BSD root: md0, major 1, minor 0`, `Serial keyboard started`,
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
`vm_free_delayed_pages: initialized 0 free pages`, `VM Swap Subsystem is ON`,
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
`load_init_program: attempting to load
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
/usr/appleinternal/sbin/launchd.development`, then `/sbin/launchd`,
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
**`*** SWEET userspace: init running as PID 1 ***`** and `SWEET init: still
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
alive` repeating (5 s heartbeat). No panic.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
**Milestone: EL0 user space runs on the Cortex-A53 with 4K pages**: Mach-O
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
load, ad-hoc code signature, syscalls, devfs /dev/console, select timeouts.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Not yet tested: dyld and the iOS dyld shared cache (need the real root).
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
## 2026-11-10: ninth boot: first eMMC probe (a510f-xnu run 42839347239, commit ca69966)
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Patch 0106 (bsd/dev/sweet_mmc.c, read-only polled-PIO DesignWare MMC
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
driver for dwmmc0 0x13540000; mmcprobe=1 prints host state + GPT in
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
IOFindBSDRoot; rd=mmcroot0 roots on GPT partition mmcroot=, default
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
USERDATA). boot-args `... rd=md0 mmcprobe=1`.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Observed: `SWEET MMC: verid 0x270a hcon 0x8e42541 ctrl 0x10 bmod 0x282
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
clkena 0x1 clkdiv 0x1`, `ctype 0x10000 uhs 0x10000 status 0x8906 fifoth
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
0x20100010 tmout 0xffffffff intmask 0x0`, `CMD13 ok, R1 0x900 (state 4, 4 =
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
transfer)`, `read lba 1 x1 failed, rintsts 0x424`, `probe FAILED (5)`; then
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
md0 root and PID 1 heartbeat as before.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Reading: DesignWare 2.70a, 64-bit FIFO (HCON H_DATA_WIDTH 2), S-Boot used
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
the IDMAC (BMOD 0x282) in 8-bit DDR (CTYPE/UHS bit 16). The card answers
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
(transfer state). 0x424 = CMD_DONE | RXDR | HTO: read data reached the FIFO
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
but was never popped. The LineageOS a5xelte config sets
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
CONFIG_MMC_DW_FORCE_32BIT_SFR_RW: Samsung reads a 64-bit FIFO entry as two
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
32-bit reads (DATA, DATA + 4); the driver used one 64-bit load.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Fix (commit cc1142b): two 32-bit FIFO reads per entry, drain before error
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
checks, HTO non-fatal while data flows, failure trace, LBA 1 bytes printed.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Fallback if PIO keeps failing: the IDMAC (64-bit descriptors of 32 words on
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
this SoC, FMP fields; DBADDRL 0x88/DBADDRU 0x8c/IDSTS 0x90/IDINTEN 0x94).
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
## 2026-11-10: tenth boot: eMMC reads work (a510f-xnu run 42843267443, commit cc1142b)
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Observed (photo): same host registers as the ninth boot, `CMD13 ok`, then
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
`SWEET MMC: LBA 1: 45 46 49 20 50 41 52 54` ("EFI PART"), `GPT: 128 entries at
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
LBA 2, disk 15028 MiB`, partitions (name start-LBA+MiB): BOTA0 8192+4,
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
BOTA1 16384+4, EFS 24576+20, CPEFS 65536+8, m9kefs1 81920+4, m9kefs2
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
90112+4, m9kefs3 98304+4, CARRIER 106496+1, PARAM 108544+8, BOOT 124928+32,
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
RECOVERY 190464+38, OTA 268288+8, CDMA-RADIO 284672+4, RADIO 292864+88,
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
TOMBSTONES 473088+1, DNT 475136+1, PERSISTENT 477184+0, PERSDATA 478208+12,
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
RESERVED2 502784+2, SYSTEM 507904+3000, CACHE 6651904+200, HIDDEN
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
7061504+60, USERDATA 7184384+11516. `probe done (0)`, then md0 root and the
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
PID 1 heartbeat as before.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
**Milestone: polled-PIO eMMC reads work** (two 32-bit FIFO reads per 64-bit
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
entry). Never touch BOTA*, EFS, CPEFS, m9kefs*, CARRIER, PARAM, RADIO,
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
PERSISTENT/PERSDATA (IMEI, modem, bootloader state).
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Next: iOS root candidate is USERDATA (11.5 GB, erases Android data; SYSTEM
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
is only 3 GB). Needed: eMMC writes (rootrw), a root image that fits, a way
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
to write it to the phone, and more RAM for iOS.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
## 2026-11-10: eMMC write support (patch 0106, renamed 0106-a510f-emmc.patch)
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
User approved USERDATA for the iOS root (Android user data is erased).
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
sweet's iOS root image has ~12 GB used, USERDATA is 11.5 GB: either trim the
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
image or use the contiguous SYSTEM..USERDATA span (~14.4 GiB, also erases
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Android SYSTEM; not approved yet).
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Driver changes:
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
- CMD24/CMD25 polled-PIO writes (two 32-bit FIFO writes per 64-bit entry,
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  pre-filled before the command, refilled while the card takes data), wait
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  for DATA_OVER, ACD (multi-block) and !DATA_BUSY; CMD6 FLUSH_CACHE on
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  DKIOCSYNCHRONIZE. Only with boot-arg `mmcrw=1`; otherwise EROFS as before.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
- `mmcroot=` takes a name or a range `A..B`; any range covering a partition
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  other than SYSTEM/CACHE/HIDDEN/USERDATA is refused (EPERM).
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
- `mmcwtest=1` (with mmcprobe=1 mmcrw=1): read the last sector of the
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  mmcroot range, write a pattern, read back, write the original back, read
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  back, flush; prints `write test LBA ...: read 0 write 0 verify OK restore
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  OK flush 0`.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Boot-args for the eleventh boot add `mmcrw=1 mmcwtest=1` (still rd=md0).
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Decision (user: "Do what is the best"): the iOS root goes on the contiguous
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
span `mmcroot=SYSTEM..USERDATA` (LBA 507904 to the end of USERDATA, ~14.4
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
GiB), so the untrimmed ~12 GB image fits with room to spare. Android no
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
longer boots afterwards; going back means flashing the stock firmware
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
(A510FXXS8CSF3) with Odin. The eleventh boot's image is repacked with
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
`mmcroot=SYSTEM..USERDATA`, so its write test also checks the range parsing
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
(it still touches only the last sector of USERDATA and restores it).
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
## 2026-11-10: eleventh boot: first eMMC write test (repack run 42852522133)
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Observed (photo): `range "SYSTEM..USERDATA": first LBA 507904, 14776 MiB`
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
(correct), `write test LBA 30769151: read 0 write 0 verify FAILED restore OK
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
flush 0`, `probe FAILED (5)`, then md0 root and PID 1 as before. LBA 30769151
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
is the last sector of USERDATA (7184384 + 11516 MiB - 1): range code is right.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
The card took the write without a CRC/timeout error (DATA_OVER), but the data
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
read back differed. "restore OK" proves little: the sector is probably all
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
zeros, and zeros survive any FIFO mangling. Suspect: two 32-bit writes to the
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
64-bit FIFO each push a whole entry (upper half zero), unlike reads.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Next boot (same boot-args): the test prints the original sector, the pattern,
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
then tries FIFO write mode 0 (2x32-bit) and mode 1 (one 64-bit store), each
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
followed by CMD13 (R1 error bits) and a read-back with mismatch count, first
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
bad offset, how many bytes still equal the old data, and the first 12 bytes.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
The working mode is kept for later writes.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
## 2026-11-10: twelfth boot: writes are silently dropped (a510f-xnu run 42853742044)
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Observed (photo): `wtest LBA 30769151 read 0, 0 non-zero bytes` (sector all
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
zeros), pattern `5a db 72 a7 ...`; mode 0 and mode 1 both: `write 0 R1
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
0x900(0) read 0: 512 bad from 0, 512 = old`, back all zeros. `FIFO write
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
mode -1 FAILED, restore OK, flush 0`.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
So the transfer completes (DATA_OVER, card back in tran/ready, no error
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
bits in CMD13) but nothing reaches the media: not FIFO mangling (mode 1
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
would differ) but most likely write protection the card reports only in the
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
CMD24 R1 (error bits are clear-on-read, so CMD13 afterwards is clean) or a
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
protection S-Boot set (USER_WP power-on / temporary WP groups).
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Next boot prints: CMD24's own R1 and RINTSTS bits, EXT_CSD (rev, SEC_COUNT,
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
PARTITION_CONFIG[179], USER_WP[171], BOOT_WP[173/174], ERASE_GROUP_DEF[175],
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
HC_WP_GRP_SIZE[221], HC_ERASE_GRP_SIZE[224], SECURE_WP_INFO[231], cache) and
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
CMD30/CMD31 write-protect status of the test sector's group.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
## 2026-11-10: thirteenth boot: not write protection (a510f-xnu run 42857637985)
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
(The user first re-flashed the previous image by mistake; that boot repeated
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
the twelfth.) Observed: `EXT_CSD 0 R1 0x900 rev 7 sec_count 30777344 (15028
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
MiB) part_cfg 0x48 user_wp 0x11 boot_wp 0x11 boot_wp_st 0x5`, `erase_grp_def
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
0 hc_wp_grp 1 hc_erase_grp 8 [231]=0x55 cache_ctrl 0 cache_size 4096`,
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
`CMD30 0 R1 0x900: 00 00 00 00`, `CMD31 ... 00 x8` (test group not
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
protected; only the boot partitions are power-on protected). Writes: `CMD24
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
R1 0x900, rintsts 0x1c` (CMD_DONE|DATA_OVER|TXDR, no errors), read back
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
`511 bad, 424 = old`, first 12 bytes zero, both FIFO modes; `restore FAILED`.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
The last USERDATA sector now holds 88 non-zero bytes (harmless: USERDATA is
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
to be overwritten anyway).
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Theory: the CPU's FIFO writes never reach the FIFO RAM; the card gets
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
whatever the last read left there (all-zero test sector before, EXT_CSD this
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
time: ~88 non-zero bytes beyond offset 12 fits). Suspect the Exynos SMU
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
(dw_mmc-exynos "eMMC protector", MPSBEGIN0/MPSEND0/MPSCTRL0 at 0x1200..,
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
MPSECURITY 0x1010): Linux sets MPSCTRL0 = 0x71 (secure write, non-secure
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
read/write, valid) before writes work.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Next boot: print the SMU registers; try 0 as left by S-Boot, then set
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
BEGIN0=0 END0=~0 CTRL0=0x71 and try FIFO modes 0 and 1. Before each write
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
the FIFO RAM is refilled with EXT_CSD (CMD8) and the read-back is compared
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
with the pattern, the old sector and EXT_CSD (non-zero span, 8 bytes).
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
## 2026-11-10: fourteenth boot: SMU open, stale FIFO data confirmed (run 42862687942)
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Observed: the test sector now reads `88 non-zero bytes` and equals EXT_CSD
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
byte for byte (`512 =EXT_CSD`) on the first read of a fresh boot: the
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
thirteenth boot's write really stored the FIFO RAM contents (EXT_CSD), not
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
the CPU's pattern. SMU as left by S-Boot: `security 0xdfe2e492 begin0 0x0
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
end0 0xffffffff ctrl0 0xf1` (all access allowed), so the SMU is not it;
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
setting ctrl0 0x71 changed nothing. All three tries: `write 0 R1 0x900 int
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
0x1c`, read back = EXT_CSD.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
So: the controller sends 512 bytes from FIFO RAM without HTO, but CPU
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
writes to DATA (0x200, 2x32 or 1x64) never land there. Our writes pre-fill
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
the FIFO before CMD24; Linux sends the command first and pushes data on
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
TXDR.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Next boot: FIFO loopback (reset, write 16 bytes, STATUS/FCNT before/after,
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
four raw 32-bit reads) for both write modes; then writes in Linux order
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
(command, then data as the FIFO drains) 2x32 and 64-bit, and prefill as the
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
control. The GPT header (LBA 1) is left in FIFO RAM before each write as the
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
stale marker; read-back is compared with pattern, EXT_CSD (old) and GPT.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
The sector is then written back to zeros (its original content).
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
## 2026-11-10: fifteenth boot: eMMC writes work (a510f-xnu run 42866358361)
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Observed: `FIFO mode 0: put 16, status 0x8906 fcnt 0 -> 0x48902 fcnt 2,
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
read 00000000 00000000 00010000 00000200 -> fcnt 2` (mode 1 the same, first
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
word 6098d746): CPU writes do count (2 entries for 16 bytes); idle reads
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
from DATA do not pop. `try 0 (on TXDR, mode 0) write 0 R1 0x900 int 0x1c
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
read 0: 0 bad`, back `5a db 72 a7 5e df 76 a3` = pattern. `write test: try
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
0 OK, zeroed OK, flush 0`, `probe done (0)`.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
**Milestone: eMMC writes work.** Fix: send CMD24/25 first and push data as
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
the FIFO drains (Linux order). Data put in the FIFO before the command is
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
lost while the count still says it is there, so the card got stale FIFO
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
RAM. 2x32-bit FIFO writes (mode 0) are right. wr_prefill stays 0.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Next: `.github/workflows/a510f-iosroot.yml` builds the iOS root on GitHub
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
(mkiosroot.sh at 14776 MiB + sweet-root-tweaks.py), splits it at the
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
SYSTEM/CACHE/HIDDEN/USERDATA boundaries into sparse system.img, cache.img,
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
hidden.img, userdata.img in one ustar Odin tar (members must stay < 8 GiB).
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
First a510f-iosroot run (42870936111): root built and tweaked fine, `11887
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
MiB used of 14776`; sparse pieces system.img 3035970408, cache.img
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
196694364, hidden.img 62824544, userdata.img 8849785560 bytes: over the
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
ustar 8 GiB member limit (tar refused). Fix: remove all localizations except
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Base/en/English/en_*, then zero the free space (deleted data would otherwise
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
stay in the sparse image).
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Third run (42874386788) succeeded after making the rm tolerant (Linux
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
hfsplus cannot remove a few non-ASCII WorkflowKit th.lproj entries): `used
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
11615 MiB (before trimming 11898)`, system.img 3013191816, cache.img
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
196694364, hidden.img 62824544, userdata.img 8572587812 bytes (17 MB under
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
the 8 GiB ustar limit), tar 11845304320 bytes, root.img sha256
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
847bdd50e51737a4..., artifact a510f-ios-root-odin (zip 6097950620 bytes).
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
First eMMC-root boot-args (repack of a510f-xnu run 42866358361): rd=mmcroot0
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
mmcroot=SYSTEM..USERDATA mmcrw=1 rootrw=1 plus sweet's iOS set
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
(unentitled_ios_sim_launch=1 ignition_level=1 wdt_test=no_user_checkin
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
launchd_unsecure_cache=1 wdt=-1); console left on (no sweetfb_noconsole).
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
## 2026-11-10: writing the iOS root to the phone (TWRP, not Odin)
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Odin: "Get PIT for mapping" ok, then `system.img FAIL!` at once, no message
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
on the download screen (SYSTEM STATUS stayed Official, FRP OFF, Secure
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Download Enabled). Tests on HIDDEN with the same 60 MiB content as sparse
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
(with FILL), sparse without FILL and raw: all three FAIL. S-Boot rejects
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
non-Samsung images for these partitions whatever the format (RECOVERY is
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
accepted).
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
TWRP for a5xelte: 3.7.0_9-0 (Android 9 base) hangs on the logo with this
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Nougat bootloader; **3.2.3-0 works** (adb as root, /dev/block/mmcblk0p20..23
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
= SYSTEM/CACHE/HIDDEN/USERDATA, starts 507904/6651904/7061504/7184384, sizes
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
match). `adb exec-in "dd of=..."` from Windows lost the last ~26 KB; what
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
works: 256 MiB raw chunks generated from the sparse tar, `adb push` to
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
/tmp (tmpfs 914 MiB), sha256 check, dd seek, read-back sha256 (scripts in
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
E:\Claude	wrp-write, ~31 s/chunk for SYSTEM, ~70 s for USERDATA). All four
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
partitions verified on the phone against the raw images:
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
SYSTEM 91f2bc0e..., CACHE 3537d735..., HIDDEN 614939a2..., USERDATA
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
b8693563... Android is gone; RECOVERY holds TWRP 3.2.3 until the kernel tar
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
is flashed back.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
## 2026-11-10: sixteenth boot: first boot of the iOS root (repack 42877251282)
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Observed: `SWEET MMC: "SYSTEM..USERDATA": first LBA 507904, 14776 MiB,
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
read-write`, `BSD root: mmcroot0`, `hfs: Initializing the journal`, `hfs:
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
iOSRoot: hfs_recording_init: creating the hotfile btree`, SWEET AMFI /
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Sandbox / HFS registered, networking up, then panic: `initproc failed to
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
start -- exit reason namespace 6 subcode 0x1 description: Library not
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
loaded: /usr/lib/libSystem.B.dylib Referenced from: <5C15DB07-...>
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
/sbin/launchd Reason: tried: '/usr/lib/libSystem.B.dylib' (no such file, no
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
dyld cache), '/usr/local/lib/libSystem.B.dylib' (no such file)`.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
**Milestone: the real launchd runs as PID 1 from the eMMC root** (dyld
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
loaded it), but dyld has no shared cache. The image is right (checked from
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
the rebuilt root.img with E:\Claude	wrp-write\hfsls.py):
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
/System/Library/Caches/com.apple.dyld holds dyld_shared_cache_arm64 and
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
.01-.42 (+ .symbols) as hard links into the OS cryptex, as on sweet.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Prime suspect: 4K pages (sweet's kernel is 16K; the cache is laid out for
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
16K). The kernel's shared-region error lines scroll away before the panic.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
0107: boot-arg initpanicdelay=SECONDS (print, then wait before the initproc
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
panic) and srtrace=N (shared_region_trace_level as a tunable; 2 = info).
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Next boot: initpanicdelay=600 srtrace=2.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
## 2026-11-10: seventeenth boot: 16K code signatures rejected (run 42903079644)
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Observed (initpanicdelay kept it on screen): libignition 1 runs (`ignition
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
level insufficient` for preboot/cryptex/graft, expected at level 1), `dylib_cache:
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
opened shared cache directory: /System/Library/Caches/com.apple.dyld`,
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
`goodbye: ignition sequence complete`, then `shared_region: ... check_np
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
... vm_shared_region_start_address() failed` (no region yet, normal), `hfs:
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
set hardlink bit ... inoid=979983975` (the cache file), **`disallowing
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
unsupported code signature page shift: 14`**, `unable to create a validated
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
cs_blob object: 85`, `dyld cache '(null)' not loaded: code signature
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
registration for shared cache failed`, then the libSystem error and `SWEET:
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
initproc failed to start; panic in 600 s`.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Cause: cs_validate_codedirectory() only takes 4K or native (here 4K) hash
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
pages; iOS signs with 16K. 0108: accept pageSize 14 when PAGE_SHIFT < 14,
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
and in cs_validate_hash() accept 4K pages covered by a 16K hash page
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
unverified (they cannot be hashed alone; the stock code would panic "offset
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
not aligned to cshash boundary"). Logged once: `SWEET: accepting 16384-byte
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
code signature pages unverified (4096-byte VM pages)`. srtrace dropped.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
## 2026-11-11: eighteenth boot: launchd starts iOS, Apple logo (run 42907039170)
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
User report (no photo yet): text scrolled fast, then many `exec xpcproxy`,
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
`exec wcd` ... lines (launchd spawning services through xpcproxy), and
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
later **the Apple logo appeared**, with the kernel console text drawn over
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
it. **Milestone: iOS userland runs and draws on the A510F screen** (through
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
the SWEET AppleCLCD/IOMobileFramebuffer stand-in).
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Next: repack with sweetfb_noconsole=1 (console muted once the GUI presents
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
its first frame, as on sweet).
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
## 2026-11-11: nineteenth boot: clean Apple logo, then black (repack 42985075608)
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Video IMG_4656.MOV (3.5 min, frames every 3 s): kernel boot to ~0:35; ~1:15
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
launchd execs UserEventAgent, keybagd, usermanagerd, logd, remoted,
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
mediaserverd, watchdogd, configd, DumpPanic, distnoted, amfid,
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
containermanagerd, bluetoothd, fairplayd.H2, backboardd, thermalmonitord,
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
sleepd, IOMFB_FDR_Loader, mtmergeprops, AppleCredentialManagerDaemon,
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
notifyd, mobiletimerd, ptpd, lockdownd, nfcd, rapportd, fseventsd,
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
identityservicesd, timed, imagent, sharingd, driverkitd, locationd, many
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
xpcproxy; ~2:00 cfprefsd, powerd, passd, runningboardd, PowerUIAgent,
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
contextstored, apfs_iosd, dasd, ACCHWComponentAuthService, mobileassetd,
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
biomed, ReportCrash, com.apple.datamigrator, lsd; `SWEET Sandbox: logd
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
privilege 1002 denied`; `CRASH driverkitd[67] sig 9`; ~2:45 `IOK
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
backboardd: matching IOProviderClass IOAcceleratorES -> 0 found` repeated
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
(no GPU, as on sweet before its CPU-rendering fixes), securityd AKS sel 7,
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
nanoprefsyncd, mobileactivationd; ~2:55 console muted, **clean Apple logo**
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
(GUI first frame); ~3:15 **black**. Matches sweet 0079: backboardd
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
RequestPowerChange(0) (auto-lock) fades the panel to black; no buttons to
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
wake it (sweetkeys=0, no A510F key driver yet).
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
0109: boot-arg sweetfb_alwayson=1 ignores display-off requests. Next boot:
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
noconsole + alwayson, to see what iOS draws after the logo.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
## 2026-11-11: twentieth boot: SpringBoard crash loop found (TWRP in RECOVERY)
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Video IMG_4657: clean Apple logo with a progress bar that crept forward,
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
then stalled for 30+ min (stray kernel lines at the screen edges). New
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
setup: iOS kernel in **BOOT** (normal power-on), **TWRP 3.2.3 in RECOVERY**
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
(tar E:\Claude510f-ios-boot+twrp-recovery.tar). From TWRP,
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
E:\Claude	wrp-write\hfsremote.py reads the iOS HFSX volume read-only over adb
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
(dd of mmcblk0 from 248 MiB, 1 MiB chunks, B-tree lookups, hard links).
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
/private/var/mobile/Library/Logs/CrashReporter: 23 SpringBoard-*.ips, one
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
every ~20 s, all the same (symbolicated by iOS): NSAssertion in
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
`-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]` <-
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
initWithScreen: <- `-[UIScreen _boundingPathUtilities]` <- `-[UIWindow
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
_boundingPath]` <- UIScrollView scroll indicator insets. Cause: our ADT has
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
**no /product node** - tools/mkadt.py copies it from Apple's D22AP device
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
tree (research/ipsw-x/d22ap.adt, not in git) and only warned when missing.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
/product carries artwork-device-subtype 2436, thin-bezel, oled-display,
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
button locations etc. Fix: workflows fetch Firmware/all_flash/
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
DeviceTree.d22ap.im4p from the IPSW and extract it (tools/im4p_extract.py,
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
LZFSE via pyliblzfse); 61 /product properties.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
## 2026-11-11: **MILESTONE: iOS 16 LOCK SCREEN ON THE GALAXY A5 2016**
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Boot from BOOT (kernel 0109 + repack 43001819608 with the D22AP /product
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
node, image E:\Claude510f-ios-boot-product.tar, TWRP 3.2.3 in RECOVERY).
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
SpringBoard no longer crash-loops: photos show the iOS 16 lock screen,
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
"Wednesday, December 31" and a clock "4:04" that advances (4:07 later).
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Observations:
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
- Date is the epoch (Dec 31 1969 local, no RTC / time source yet).
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
- Clock and date drawn in red (iOS draws them white on the default
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  wallpaper; wallpaper itself black): check the pixel format / channel
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  order of the SWEET FB copy to the DECON (ARGB8888) and the wallpaper path.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
- Kernel console text briefly drew over the GUI, then disappeared.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
- No touch (sweettouch=0, no A510F touch driver), no buttons (sweetkeys=0).
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
- Screen stays on (sweetfb_alwayson=1).
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Next: A510F touch driver (touch IC on the I2C bus, see the LineageOS DT),
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
buttons (gpio-keys: Home, Vol; power key via PMIC), RTC time, colours.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
## 2026-11-11: touchscreen driver (0110, bsd/dev/a510f_touch.c)
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Hardware (LineageOS a5xelte DT + TWRP 3.2.3 sysfs/debugfs, where touch
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
works): Zinitix ZT7538 (bt532_ts_device) at 10-0020 = 0x20 on the s3c2410
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
I2C at 0x13850000 (pins gpc3-0/1 function 2, pull-up 3; pclk gate
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
CMU_PERI 0x139F0904 bit 9), attention gpa1-1 (0x139B0020 bank, active low).
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Supply tsp_avdd = S2MPU03 LDO33 (3.3 V, not boot-on), PMIC 3-a066 on HSI2C3
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
0x104C0000 with Samsung's batcher (opcode/payload sequence copied from
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
i2c-exynos5.c exynos5_i2c_xfer_batcher; reads use 10-bit mode). L33CTRL =
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
0x4E, on = 0xFC ([7:6]=11, vsel 0x3C = 3.3 V). TWRP has no /dev/mem.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Display: the 1080x1920 panel shows the centre of the 1125x2436 frame (y
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
offset 258), SweetHIDTouch adds 18, so the driver adds 240 to y.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Driver (one polled kernel thread, started from sweet_mmc_init): a510ftouch=1
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
probes and prints (chip before power, PMIC ID, LDO33), =2 also switches
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
LDO33 on (only if the PMIC reads are sane and the LDO reads 3.3 V-selected),
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
runs the BT532 power sequence (0xc000/0xc004/0xc002/0xc001) + mini init
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
(SWRESET, TOUCH_MODE 0, INT mask 0x3f, clear x10), then polls gpa1-1 and
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
reads 0x0080 (status, count, 6 bytes/finger) -> sweet_hid_touch.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
First touch boot (run 43007348036, BOOT): `A510F TOUCH: mode 2, PERIC pclk
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
0x53fbfff, gpc3 con 0x22 pud 0x5f, gpa1 con 0x0 dat 0x2, iiccon 0xaf
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
iicstat 0x10, hsi2c ctl 0x0 conf 0x9803c1ff batcher con 0x0 state 0x8`;
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
`chip at 0x20 before power: 6` (ENXIO, no ACK: unpowered); `batcher write
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
failed: state 0x200 fifo 0x1000001 int 0x1` twice; PMIC id/LDO33 not read;
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
`PMIC reads not trusted, LDO33 left alone` (guard worked). Completion is
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
BATCHER_INT_STATUS bit 0 (Samsung's IRQ handler sets the state COMPLETE bit
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
itself): fixed in 0110.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Plan (user, 2026-11-11): after touch works, switch the userland from the
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
iPhone X (D22AP, 1125x2436, no Home button) to the **iPhone 8 Plus**
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
(iPhone10,2 D21AP: 1242x2208 rendered and scaled to a 1080x1920 16:9 panel,
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Home button) - same A11 generation, matches the A510F panel and Home key.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Needs: root image from the 8 Plus IPSW, D21AP /product, identity patch
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
(sweet 0059 says iPhone10,3/D22AP), logical display 1242x2208, scale to fit
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
(0111 sweetfb_fit, written in ref/p0109, not pushed yet), touch mapping.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
Second touch boot (run 43011405392): `PMIC id 0 0x77, LDO33 ctrl 0 0x77`:
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
the batcher messages now complete but the RX payload keeps the 0x77
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
placeholder (no byte received); guard held. S-Boot leaves HSI2C3 in plain
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
auto mode (conf 0x9803c1ff, batcher con 0). 0110 now tries plain polled
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
HSI2C first (exynos5_i2c_xfer_msg polling path: 7-bit 0x66, write reg
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
without stop, read 1 with stop), then the batcher, printing hs INT/TRANS/
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
FIFO status after every message; LDO33 is written through whichever path
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
returns a sane ID and a 3.3 V-selected L33CTRL.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
**Touch boots 3 and 4 (2026-11-11), both froze the phone.**
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
- touch3 (plain mode): HSI2C3 TRANS_STATUS 0x2000c, TX FIFO kept the byte
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  (fifo 0x1000001), `plain PMIC id 5 0xee`; the batcher step after it never
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  printed and the whole phone froze.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
- touch4 (HSI2C SW_RST keeping S-Boot timing, then plain, then batcher):
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  saved conf 0x9803c1ff fs1 0xf0f0f00 fs2 0xf0ffffff fs3 0xff00ff sla 0xff;
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  after reset ctl 0x9 but trans still 0x2000c, fifo 0x1000100; plain gave
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  "bus not idle" (EBUSY); after "trying the batcher" + reset the phone froze.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
- Samsung's kernel (ref/k7580): hsi2c@104c0000 has `samsung,hsi2c-batcher`,
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  HS mode 2.5 MHz, a second reg at 0x104b0180 (mailbox), pins gpm0-0 SDA /
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  gpm0-1 SCL (pinctrl 0x104E0000), pclk_hsi2c3 = CMU_MIF 0x10430900 bit 27.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  The bus is shared with the APM (Cortex-M3) behind a hardware semaphore
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  (HSI2C_SMRelease 0x200) that the batcher takes. Conclusion (guess, fits
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  both freezes): never touch the HSI2C registers directly.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
- touch5 (commit de5330e): batcher only, read-only dump of pclk/gpm0/batcher
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  state first, batcher state trace + payload per message. Its first CI run
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  failed in the ISA check on an Ubuntu apt mirror error (exit 100), the
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  rerun (6ad6487) hung on apt; the workflow now takes numpy from PyPI and
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  puts timeouts/retries on apt.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
- touch5 (local image: CI apt mirror down, boot image spliced on the PC with
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  a510f/tools/splice_payload.py from the CI kernel artifact): pclk_hsi2c3 on
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  (MIF 0x900 = 0x1f79f0ff), **gpm0 con 0x11 dat 0x3**: S-Boot leaves the PMIC
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  bus pins as GPIO outputs, not HSI2C. Froze after `bat wr states 0x40 0x200`
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  on an HSI2C status read while the batcher owned the block (same read as
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  touch3/4: that, not the plain mode itself, is what froze them).
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
- touch6 (gpm0 -> func 2, pud 3, drv 2; no HSI2C reads during batcher):
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  no freeze, boots to the lock screen. Write reg 0x00: states 0x40 -> 0x11,
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  int 0x81, idle after. Read stopped early on a stale INT_STATUS 0x81 ->
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  0x77, batcher left in 0x200.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
- touch7 (done = state bit 0, reset stuck batcher + SMRelease): write OK as
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  before; the 10-bit EXT_ADDR read goes 0x40 -> 0x200 and stays there 200 ms
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  (no RX interrupt). Batcher reset works (0x200 -> 0x8).
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
- touch8 (commit c84c53c): enables TRANSFER_DONE + 0xf00 trans-state error
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
- touch8 result: PMIC read form **stop+7bit** works (id 0x02, L33CTRL 0x3c),
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  LDO33 -> 0xfc, ZT7538 chip code 0xe538, vendor 0x5a49 ("ZI"), fw 0x0005.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  The 10-bit EXT_ADDR read gets UNEXP (int 0x400 = no-dev-ack).
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
- **🎉 TOUCH WORKS (touch9, commit d80cb34, 2026-11-11 ~19:00 local,
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  video IMG_4691.MOV):** single and multi-finger touches reach iOS; holding
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  the lock screen opens the wallpaper/customise UI. Fixes in touch9: the poll
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  loop always sleeps 8 ms (it used to re-poll without sleeping while attn was
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  low, busy-waiting I2C on the only CPU), skips status 0/1/0xffff/MUST_ZERO
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  reports. That boot ran with sweetfb_noconsole=0 (console over the UI).
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  Input is slow (cpus=1; sweet saw ~1 min latency on 1 core). Next: GPIO
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  buttons (gpa2) -> sweet_hid_key, noconsole back to 1, then iPhone 8 Plus
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  userland, then SMP (PSCI cpu_on 0xC4000003, MPIDR 0x000-0x003, 0x100-0x103).
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  interrupts, tries 4 read forms (nostop+10bit, stop+7bit, nostop+7bit,
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  stop+10bit), one console line per message. Not booted yet.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
- Facts checked in Samsung's source: L33CTRL really is 0x4E (enum has explicit
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  jumps), LDO33 "tsp_avdd" is the only touch supply (`zinitix,gpio_ldo_en`
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  only means "no separate dvdd regulator"), ZT7538 int mask 0x3f (palm on),
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
  touch mode 0, x/y resolution 1080x1920.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
## Open problems before XNU work
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).

- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
1. **16 KB pages.** XNU arm64 builds its kernel pmap on a 16 KB granule.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
   xnu-8796 has 4 KB page-table attributes (`pmap_pt_attr_4k`, used for
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
   Rosetta processes on Apple silicon); the port needs the kernel's native
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
   attributes switched to 4 KB. iOS binaries are 16 KB aligned, which is also
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
   4 KB aligned.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
2. **LSE atomics.** Check whether the iPhone X iOS 16.7 dyld_shared_cache
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
   uses CAS/LDADD/SWP etc. If it does, trap and emulate them in the kernel
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
   (undefined-instruction handler), at a speed cost.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
3. eMMC driver (DW-MMC), GICv2, Exynos HS-I2C touch, S2MPU05 PMIC: new
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
   drivers compared to sweet.
- Buttons boot (commit 7f545e1, IMG_4697): Home closes the lock-screen
  editor, volume shows the iOS HUD, Power turns the display off/on. Crash
  reports pulled from the phone in TWRP (twrp-write/hfsremote.py, read-only,
  pulled/b4697): every SpringBoard crash is the iPhone X screen-shape
  assertion `-[_UIScreenComplexBoundingPathUtilities _loadBitmapForScreen:type:]`,
  triggered on display-on (`didGainControlOfDisplay`) and other layouts.
  Notched devices only -> the iPhone 8 Plus switch removes it.
- **iPhone 8 Plus switch (started 2026-11-11 evening):** IPSW
  iPhone_5.5_P3_16.7.16_20H392 (same build as the X one). a510f-iosroot.yml
  builds the 8 Plus root (artifact a510f-ios-root-8plus-odin);
  mkadt_a510f.py: iPhone10,2 / D21AP, canvas 1242x2208, /product and
  /buttons (button-names, home-button-type, opposed-power-vol-buttons only)
  from DeviceTree.d21ap.im4p (CI fetch into research/ipsw-8p, git-ignored);
  0111 scale-to-fit + 0112 (1242x2208 @401 ppi, SweetHID touch 1:1 on
  1080x1920 with sweetfb_fit, edge detection on the real panel);
  boot-arg sweetfb_fit=1; a510f_touch.c drops the +240 y offset with fit.
  The new boot image needs the new root (identity mismatch otherwise).
