# -*- coding: utf-8 -*-

# 16진수로 되어있는 TAGS의 키값을 10진수로 바꿔보는 방법
#print hex(36867)
#print 0x9003


# ExifTags.py에 있는 이미지 정보의 키,값 dict
TAGS = {

    # possibly incomplete
    0x0100: "ImageWidth",
    0x0101: "ImageLength",
    0x0102: "BitsPerSample",
    0x0103: "Compression",
    0x0106: "PhotometricInterpretation",
    0x010e: "ImageDescription",
    0x010f: "Make",
    0x0110: "Model",
    0x0111: "StripOffsets",
    0x0112: "Orientation",
    0x0115: "SamplesPerPixel",
    0x0116: "RowsPerStrip",
    0x0117: "StripByteConunts",
    0x011a: "XResolution",
    0x011a: "XResolution",
    0x011b: "YResolution",
    0x011b: "YResolution",
    0x011c: "PlanarConfiguration",
    0x0128: "ResolutionUnit",
    0x0128: "ResolutionUnit",
    0x012d: "TransferFunction",
    0x0131: "Software",
    0x0132: "DateTime",
    0x013b: "Artist",
    0x013e: "WhitePoint",
    0x013f: "PrimaryChromaticities",
    0x0201: "JpegIFOffset",
    0x0202: "JpegIFByteCount",
    0x0211: "YCbCrCoefficients",
    0x0211: "YCbCrCoefficients",
    0x0212: "YCbCrSubSampling",
    0x0213: "YCbCrPositioning",
    0x0213: "YCbCrPositioning",
    0x0214: "ReferenceBlackWhite",
    0x0214: "ReferenceBlackWhite",
    0x1000: "RelatedImageFileFormat",
    0x1001: "RelatedImageLength",
    0x1001: "RelatedImageWidth",
    0x828d: "CFARepeatPatternDim",
    0x828e: "CFAPattern",
    0x828f: "BatteryLevel",
    0x8298: "Copyright",
    0x829a: "ExposureTime",
    0x829d: "FNumber",
    0x8769: "ExifOffset",
    0x8773: "InterColorProfile",
    0x8822: "ExposureProgram",
    0x8824: "SpectralSensitivity",
    0x8825: "GPSInfo",
    0x8827: "ISOSpeedRatings",
    0x8828: "OECF",
    0x8829: "Interlace",
    0x882a: "TimeZoneOffset",
    0x882b: "SelfTimerMode",
    0x9000: "ExifVersion",
    0x9003: "DateTimeOriginal",
    0x9004: "DateTimeDigitized",
    0x9101: "ComponentsConfiguration",
    0x9102: "CompressedBitsPerPixel",
    0x9201: "ShutterSpeedValue",
    0x9202: "ApertureValue",
    0x9203: "BrightnessValue",
    0x9204: "ExposureBiasValue",
    0x9205: "MaxApertureValue",
    0x9206: "SubjectDistance",
    0x9207: "MeteringMode",
    0x9208: "LightSource",
    0x9209: "Flash",
    0x920a: "FocalLength",
    0x920b: "FlashEnergy",
    0x920c: "SpatialFrequencyResponse",
    0x920d: "Noise",
    0x9211: "ImageNumber",
    0x9212: "SecurityClassification",
    0x9213: "ImageHistory",
    0x9214: "SubjectLocation",
    0x9215: "ExposureIndex",
    0x9216: "TIFF/EPStandardID",
    0x927c: "MakerNote",
    0x9286: "UserComment",
    0x9290: "SubsecTime",
    0x9291: "SubsecTimeOriginal",
    0x9292: "SubsecTimeDigitized",
    0xa000: "FlashPixVersion",
    0xa001: "ColorSpace",
    0xa002: "ExifImageWidth",
    0xa003: "ExifImageHeight",
    0xa004: "RelatedSoundFile",
    0xa005: "ExifInteroperabilityOffset",
    0xa20b: "FlashEnergy",
    0xa20c: "SpatialFrequencyResponse",
    0xa20e: "FocalPlaneXResolution",
    0xa20f: "FocalPlaneYResolution",
    0xa210: "FocalPlaneResolutionUnit",
    0xa214: "SubjectLocation",
    0xa215: "ExposureIndex",
    0xa217: "SensingMethod",
    0xa300: "FileSource",
    0xa301: "SceneType",
    0xa302: "CFAPattern",

}

# 이미지 정보가 테스트 삼아 있다고 생각한 dict
test = {
	0x010f:"LG",
	0x010f:"LG-SFD",
	0x9003:"2014-07-31",
	0x9004:"2014-05-22"
}

# 소스에 있는 부분을 나타낸 부분
lis = [(TAGS.get(key,key), str(value).decode('utf-8,','ignore'))
	for key, value in test.items()
	if type(TAGS.get(key,key)) is str]

print lis

print

# (키,값)을 나열한 리스트 예제
wow = [ (10,29), (22,50), ("Make","LG") ]
print wow
