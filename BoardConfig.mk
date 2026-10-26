#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

# Build the kernel, DTB(O) and modules from source
TARGET_OPT_IN_OSS_KERNEL := true

# Partitions
BOARD_SUPER_PARTITION_SIZE := 9663676416

DEVICE_PATH := device/xiaomi/aurora

# Include the common chipset BoardConfig.
include device/xiaomi/sm8650-common/BoardConfigCommon.mk

# Assert
TARGET_OTA_ASSERT_DEVICE := aurora

# Display
TARGET_SCREEN_DENSITY := 560

# Kernel
# Our kernel ships gki_defconfig + vendor/pineapple_GKI.config + vendor/aurora_GKI.config
# (no vendor/xiaomi/sm8650_GKI.config split), so override the common default.
# The aurora DTB(O) is built as part of the pineapple dtbo set, no product flag needed.
TARGET_KERNEL_CONFIG := \
    gki_defconfig \
    vendor/pineapple_GKI.config \
    vendor/aurora_GKI.config

# Properties
TARGET_ODM_PROP += $(DEVICE_PATH)/properties/odm.prop
TARGET_VENDOR_PROP += $(DEVICE_PATH)/properties/vendor.prop

# Include the proprietary files BoardConfig.
-include vendor/xiaomi/aurora/BoardConfigVendor.mk
