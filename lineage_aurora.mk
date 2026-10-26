#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from those products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit_only.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)

# Inherit from aurora device
$(call inherit-product, device/xiaomi/aurora/device.mk)

# Inherit some common Lineage stuff.
$(call inherit-product, vendor/lineage/config/common_full_phone.mk)

PRODUCT_NAME := lineage_aurora
PRODUCT_DEVICE := aurora
PRODUCT_MANUFACTURER := Xiaomi
PRODUCT_BRAND := Xiaomi
PRODUCT_MODEL := 24030PN60G

PRODUCT_GMS_CLIENTID_BASE := android-xiaomi

PRODUCT_BUILD_PROP_OVERRIDES += \
    BuildDesc="aurora_global-user 16 BP2A.250605.031.A3 16OS3.1.260922.212507795.QCPEGL.S release-keys" \
    BuildFingerprint=Xiaomi/aurora_global/aurora:16/BP2A.250605.031.A3/16OS3.1.260922.212507795.QCPEGL.S:user/release-keys \
    DeviceName=aurora \
    DeviceProduct=aurora_global \
    SystemDevice=aurora \
    SystemName=aurora_global
