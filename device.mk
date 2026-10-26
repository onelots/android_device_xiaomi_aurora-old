#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from sm8650-common
$(call inherit-product, device/xiaomi/sm8650-common/common.mk)

# Get non-open-source specific aspects
$(call inherit-product, vendor/xiaomi/aurora/aurora-vendor.mk)

# Soong namespaces
PRODUCT_SOONG_NAMESPACES += \
    $(LOCAL_PATH)

# TODO: device overlays (FrameworksResAurora / SystemUIResAurora) for the
# 1440x3200 N1 panel once display tuning starts; common provides generics.
