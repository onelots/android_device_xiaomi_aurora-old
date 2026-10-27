#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)
from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixups,
    lib_fixups_user_type,
)

namespace_imports = [
    'device/xiaomi/sm8650-common',
    'vendor/xiaomi/sm8650-common',
    'hardware/qcom-caf/sm8650',
    'hardware/xiaomi',
    'vendor/qcom/opensource/commonsys-intf/display',
]

def lib_fixup_odm_suffix(lib: str, partition: str, *args, **kwargs):
    return f'{lib}_{partition}' if partition == 'odm' else None


lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    (
        'sqlite3',
        'libqshcamera',
    ): lib_fixup_odm_suffix,
}

# Camera blobs link against the old graphics.allocator-V1; realign to V2.
_graphics_allocator_v1_blobs = (
    'odm/bin/aecxsimulator',
    'odm/lib64/camera/com.qti.actuator.aurora_ofilm_imx858_gt9764v_tele3x_actuator.so',
    'odm/lib64/camera/com.qti.actuator.aurora_semco_imx858_ak7316_ultra_actuator.so',
    'odm/lib64/camera/com.qti.actuator.aurora_semco_imx858_sem1217s_tele5x_actuator.so',
    'odm/lib64/camera/com.qti.actuator.aurora_semco_LYT900_ak7316_wide_actuator.so',
    'odm/lib64/camera/com.qti.aperture.aurora_semco_LYT900_ak7316_wide_aperture.so',
    'odm/lib64/camera/com.qti.eeprom.aurora_ofilm_imx858_gt24p128f_tele3x_eeprom.so',
    'odm/lib64/camera/com.qti.eeprom.aurora_ofilm_ov32b40_p24c64e_front_eeprom.so',
    'odm/lib64/camera/com.qti.eeprom.aurora_semco_imx858_p24c128f_ultra_eeprom.so',
    'odm/lib64/camera/com.qti.eeprom.aurora_semco_imx858_sem1217s_tele5x_eeprom.so',
    'odm/lib64/camera/com.qti.eeprom.aurora_semco_LYT900_p24c512x_wide_eeprom.so',
    'odm/lib64/camera/com.qti.ois.aurora_tele3x_bu24618_ois.so',
    'odm/lib64/camera/com.qti.ois.aurora_tele5x_sem1217s_ois.so',
    'odm/lib64/camera/com.qti.ois.aurora_wide_bu24631_ois_i.so',
    'odm/lib64/camera/com.qti.sensor.aurora_ofilm_imx858_tele3x.so',
    'odm/lib64/camera/com.qti.sensor.aurora_ofilm_ov32b40_front.so',
    'odm/lib64/camera/com.qti.sensor.aurora_semco_imx858_tele5x.so',
    'odm/lib64/camera/com.qti.sensor.aurora_semco_imx858_ultra.so',
    'odm/lib64/camera/com.qti.sensor.aurora_semco_LYT900_wide.so',
    'odm/lib64/camera/components/com.jigan.node.videobokeh.so',
    'odm/lib64/camera/components/com.mi.node.aiasd.so',
    'odm/lib64/camera/components/com.mi.node.rearvideo.so',
    'odm/lib64/camera/components/com.mi.node.videobokeh.so',
    'odm/lib64/camera/components/com.mi.node.videofilter.so',
    'odm/lib64/camera/components/com.mi.node.videonight.so',
    'odm/lib64/camera/components/com.qti.hwcfg.bps.so',
    'odm/lib64/camera/components/com.qti.hwcfg.ife.so',
    'odm/lib64/camera/components/com.qti.hwcfg.ipe.so',
    'odm/lib64/camera/components/com.qti.node.aon.so',
    'odm/lib64/camera/components/com.qti.node.depth.so',
    'odm/lib64/camera/components/com.qti.node.depthprovider.so',
    'odm/lib64/camera/components/com.qti.node.dewarp.so',
    'odm/lib64/camera/components/com.qti.node.eisv2.so',
    'odm/lib64/camera/components/com.qti.node.eisv3.so',
    'odm/lib64/camera/components/com.qti.node.evadepth.so',
    'odm/lib64/camera/components/com.qti.node.gme.so',
    'odm/lib64/camera/components/com.qti.node.gyrornn.so',
    'odm/lib64/camera/components/com.qti.node.hdr10pgen.so',
    'odm/lib64/camera/components/com.qti.node.hdr10phist.so',
    'odm/lib64/camera/components/com.qti.node.itofpreprocess.so',
    'odm/lib64/camera/components/com.qti.node.ml.so',
    'odm/lib64/camera/components/com.qti.node.mlinference.so',
    'odm/lib64/camera/components/com.qti.node.pixelstats.so',
    'odm/lib64/camera/components/com.qti.node.seg.so',
    'odm/lib64/camera/components/com.qti.node.swec.so',
    'odm/lib64/camera/components/com.qti.node.swregistration.so',
    'odm/lib64/camera/components/com.qti.node.swvrt.so',
    'odm/lib64/camera/components/com.qti.stats.cnndriver.so',
    'odm/lib64/camera/components/com.xiaomi.node.smooth_transition.so',
    'odm/lib64/camera/components/libcamxevainterface.so',
    'odm/lib64/camera/components/libdepthmapwrapper_itof.so',
    'odm/lib64/camera/components/libdepthmapwrapper_secure.so',
    'odm/lib64/camera/libchxlogicalcameratable.so',
    'odm/lib64/com.qti.camx.chiiqutils.so',
    'odm/lib64/com.qti.chiusecaseselector.so',
    'odm/lib64/com.qti.feature2.afbrckt.so',
    'odm/lib64/com.qti.feature2.demux.so',
    'odm/lib64/com.qti.feature2.derivedoffline.so',
    'odm/lib64/com.qti.feature2.fusion.so',
    'odm/lib64/com.qti.feature2.generic.so',
    'odm/lib64/com.qti.feature2.gs.sm8650.so',
    'odm/lib64/com.qti.feature2.hdr.so',
    'odm/lib64/com.qti.feature2.mcreprocrt.so',
    'odm/lib64/com.qti.feature2.memcpy.so',
    'odm/lib64/com.qti.feature2.metadataserializer.so',
    'odm/lib64/com.qti.feature2.mfsr.so',
    'odm/lib64/com.qti.feature2.ml.so',
    'odm/lib64/com.qti.feature2.mux.so',
    'odm/lib64/com.qti.feature2.offlinestatsregeneration.so',
    'odm/lib64/com.qti.feature2.qcfa.so',
    'odm/lib64/com.qti.feature2.rawhdr.so',
    'odm/lib64/com.qti.feature2.realtimeserializer.so',
    'odm/lib64/com.qti.feature2.rt.so',
    'odm/lib64/com.qti.feature2.rtmcx.so',
    'odm/lib64/com.qti.feature2.serializer.so',
    'odm/lib64/com.qti.feature2.statsregeneration.so',
    'odm/lib64/com.qti.feature2.stub.so',
    'odm/lib64/com.qti.feature2.swmf.so',
    'odm/lib64/com.qti.qseeutils.so',
    'odm/lib64/com.qualcomm.mcx.distortionmapper.so',
    'odm/lib64/com.qualcomm.mcx.linearmapper.so',
    'odm/lib64/com.qualcomm.mcx.nonlinearmapper.so',
    'odm/lib64/com.qualcomm.mcx.policy.mfl.so',
    'odm/lib64/com.qualcomm.qti.mcx.usecase.extension.so',
    'odm/lib64/com.xiaomi.camx.hook.so',
    'odm/lib64/com.xiaomi.chi.hook.so',
    'odm/lib64/hw/camera.qcom.sm8650.so',
    'odm/lib64/hw/camera.qcom.so',
    'odm/lib64/hw/com.qti.chi.offline.so',
    'odm/lib64/hw/com.qti.chi.override.so',
    'odm/lib64/libcamerapostproc.so',
    'odm/lib64/libcamxhwnodecontext.so',
    'odm/lib64/libcamxifestriping.so',
    'odm/lib64/libcamximageformatutils.so',
    'odm/lib64/libcamxncsdatafactory.so',
    'odm/lib64/libchifeature2.so',
    'odm/lib64/libcom.xiaomi.mawutilsold.so',
    'odm/lib64/libcommonchiutils.so',
    'odm/lib64/libfastmessage.so',
    'odm/lib64/libhme.so',
    'odm/lib64/libipebpsstriping.so',
    'odm/lib64/libipebpsstriping170.so',
    'odm/lib64/libipebpsstriping480.so',
    'odm/lib64/libisphwsetting.so',
    'odm/lib64/libjpege.so',
    'odm/lib64/libmctfengine_stub.so',
    'odm/lib64/libmfec.so',
    'odm/lib64/libmmcamera_bestats.so',
    'odm/lib64/libmmcamera_cac.so',
    'odm/lib64/libmmcamera_lscv35.so',
    'odm/lib64/libmmcamera_pdpc.so',
    'odm/lib64/libofflinefeatureintf.so',
    'odm/lib64/libopestriping.so',
    'odm/lib64/libqimagebuffer.so',
    'odm/lib64/libtfestriping.so',
    'odm/lib64/libubifocus.so',
    'odm/lib64/vendor.qti.hardware.camera.aon-service-impl.so',
    'odm/lib64/vendor.qti.hardware.camera.offlinecamera-service-impl.so',
    'odm/lib64/vendor.qti.hardware.camera.postproc@1.0-service-impl.so',
)

blob_fixups: blob_fixups_user_type = {
    (
        'odm/etc/camera/enhance_motiontuning.xml',
        'odm/etc/camera/motiontuning.xml',
        'odm/etc/camera/night_enhance_motiontuning.xml',
        'odm/etc/camera/night_motiontuning.xml',
    ): blob_fixup()
        .regex_replace('xml=version', 'xml version'),
    'odm/bin/hw/vendor.xiaomi.hardware.vibratorfeature.service': blob_fixup()
        .replace_needed(
            'android.hardware.vibrator-V1-ndk_platform.so',
            'android.hardware.vibrator-V1-ndk.so',
        ),
    'odm/bin/hw/mfp-daemon': blob_fixup()
        .replace_needed(
            'android.hardware.biometrics.common-V3-ndk.so',
            'android.hardware.biometrics.common-V4-ndk.so',
        )
        .replace_needed(
            'android.hardware.biometrics.fingerprint-V3-ndk.so',
            'android.hardware.biometrics.fingerprint-V4-ndk.so',
        ),
    (
        'vendor/lib64/vendor.xiaomi.hardware.camera.injection-V1-ndk.so',
        'vendor/lib64/vendor.xiaomi.hardware.camera.injection-client.so',
        'vendor/lib64/vendor.xiaomi.hardware.camera.injection-service.so',
    ): blob_fixup()
        .replace_needed(
            'android.hardware.camera.device-V1-ndk.so',
            'android.hardware.camera.device-V2-ndk.so',
        ),
    _graphics_allocator_v1_blobs: blob_fixup()
        .replace_needed(
            'android.hardware.graphics.allocator-V1-ndk.so',
            'android.hardware.graphics.allocator-V2-ndk.so',
        ),
    (
        'odm/lib64/libAncHumanVideoBokehV4.so',
        'odm/lib64/libTrueSight.so',
        'odm/lib64/libMiPhotoFilter.so',
        'odm/lib64/libwa_widelens_undistort.so',
        'odm/lib64/libmorpho_ubwc.so'
    ): blob_fixup()
        .clear_symbol_version('AHardwareBuffer_allocate')
        .clear_symbol_version('AHardwareBuffer_describe')
        .clear_symbol_version('AHardwareBuffer_isSupported')
        .clear_symbol_version('AHardwareBuffer_lock')
        .clear_symbol_version('AHardwareBuffer_lockPlanes')
        .clear_symbol_version('AHardwareBuffer_release')
        .clear_symbol_version('AHardwareBuffer_unlock'),
    (
        'odm/lib64/hw/camera.qcom.so',
        'odm/lib64/hw/com.qti.chi.override.so',
        'odm/lib64/libchifeature2.so',
        'odm/lib64/libcamxcommonutils.so',
        'odm/lib64/libmialgoengine.so',
        'vendor/lib64/libcameraopt.so',
    ): blob_fixup()
        .add_needed('libprocessgroup_shim.so'),
    'odm/lib64/com.qti.feature2.anchorsync.so': blob_fixup()
        .replace_needed(
            'android.hardware.graphics.allocator-V1-ndk.so',
            'android.hardware.graphics.allocator-V2-ndk.so',
        )
        .replace_needed(
            'libtinyxml2.so',
            'libtinyxml2-v34.so',
        ),
    (
        'odm/bin/hw/vendor.xiaomi.sensor.tofsensorservice.aidl',
        'odm/lib64/camera/plugins/com.xiaomi.plugin.anchor.so',
        'odm/lib64/camera/plugins/com.xiaomi.plugin.mialgoaiur.so',
        'odm/lib64/camera/plugins/com.xiaomi.plugin.mialgosnsc.so',
    ): blob_fixup()
        .replace_needed(
            'libtinyxml2.so',
            'libtinyxml2-v34.so',
        ),
    (
        'odm/lib64/camera/plugins/com.xiaomi.plugin.gainmap.so',
        'odm/lib64/camera/plugins/com.xiaomi.plugin.jpegrAggr.so',
    ): blob_fixup()
        .replace_needed(
            'libultrahdr.so',
            'libultrahdr_prebuilt.so',
        ),
    'vendor/lib64/libultrahdr_prebuilt.so': blob_fixup()
        .replace_needed(
            'libjpegdecoder.so',
            'libjpegdecoder_prebuilt.so',
        )
        .replace_needed(
            'libjpegencoder.so',
            'libjpegencoder_prebuilt.so',
        ),
}

module = ExtractUtilsModule(
    'aurora',
    'xiaomi',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
    check_elf=True,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
