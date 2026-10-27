#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

# Use the prebuilt stock kernel, DTB(O) and modules (see Kernel below)
TARGET_OPT_IN_OSS_KERNEL := false

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
# Ship the stock OS3.0.305.0 kernel, DTB(O) and modules from device/xiaomi/aurora-kernel.
# The kernel source is kept for the generated kernel headers only.
KERNEL_PATH := $(DEVICE_PATH)-kernel

TARGET_KERNEL_SOURCE := kernel/xiaomi/sm8650
TARGET_KERNEL_CONFIG := \
    gki_defconfig \
    vendor/pineapple_GKI.config \
    vendor/aurora_GKI.config
TARGET_FORCE_PREBUILT_KERNEL := true
TARGET_PREBUILT_KERNEL := $(KERNEL_PATH)/kernel

BOARD_PREBUILT_DTBIMAGE_DIR := $(KERNEL_PATH)/dtb
BOARD_PREBUILT_DTBOIMAGE := $(KERNEL_PATH)/dtbo.img

BOARD_VENDOR_RAMDISK_KERNEL_MODULES := $(wildcard $(KERNEL_PATH)/vendor_ramdisk/*.ko)
BOARD_VENDOR_RAMDISK_KERNEL_MODULES_LOAD := $(strip $(shell cat $(KERNEL_PATH)/vendor_ramdisk/modules.load))
BOARD_VENDOR_RAMDISK_RECOVERY_KERNEL_MODULES_LOAD := $(strip $(shell cat $(KERNEL_PATH)/vendor_ramdisk/modules.load.recovery))
BOARD_VENDOR_RAMDISK_KERNEL_MODULES_BLOCKLIST_FILE := $(KERNEL_PATH)/vendor_ramdisk/modules.blocklist

BOARD_VENDOR_KERNEL_MODULES := $(wildcard $(KERNEL_PATH)/vendor_dlkm/*.ko)
BOARD_VENDOR_KERNEL_MODULES_LOAD := $(strip $(shell cat $(KERNEL_PATH)/vendor_dlkm/modules.load))
BOARD_VENDOR_KERNEL_MODULES_BLOCKLIST_FILE := $(KERNEL_PATH)/vendor_dlkm/modules.blocklist

BOARD_SYSTEM_KERNEL_MODULES := $(shell find $(KERNEL_PATH)/system_dlkm -name '*.ko')
BOARD_SYSTEM_KERNEL_MODULES_LOAD := $(notdir $(strip $(shell cat $(KERNEL_PATH)/system_dlkm/modules.load)))

# Properties
TARGET_ODM_PROP += $(DEVICE_PATH)/properties/odm.prop
TARGET_VENDOR_PROP += $(DEVICE_PATH)/properties/vendor.prop

# Include the proprietary files BoardConfig.
-include vendor/xiaomi/aurora/BoardConfigVendor.mk
