AR = 'arm-none-eabi-ar'
ARFLAGS = 'rcs'
AS = 'arm-none-eabi-gcc'
BINDIR = '/usr/local/bin'
BLOCK_MESSAGE_KEYS = []
BUILD_DIR = 'basalt'
BUILD_TYPE = 'app'
BUNDLE_BIN_DIR = 'basalt'
BUNDLE_NAME = 'pebble-World-Cup.pbw'
CC = ['arm-none-eabi-gcc']
CCLNK_SRC_F = []
CCLNK_TGT_F = ['-o']
CC_NAME = 'gcc'
CC_SRC_F = []
CC_TGT_F = ['-c', '-o']
CC_VERSION = ('4', '7', '2')
CFLAGS = ['-mcpu=cortex-m3', '-mthumb', '-ffunction-sections', '-fdata-sections', '-g', '-fPIE', '-Os', '-D_TIME_H_', '-Wall', '-Wextra', '-Werror', '-Wno-unused-parameter', '-Wno-error=unused-function', '-Wno-error=unused-variable', '-std=c11', '-fms-extensions', '-Wno-address', '-Wno-type-limits', '-Wno-missing-field-initializers']
CFLAGS_MACBUNDLE = ['-fPIC']
CFLAGS_cshlib = ['-fPIC']
CPPPATH_ST = '-I%s'
DEFINES = ['RELEASE', 'PBL_PLATFORM_BASALT', 'PBL_COLOR', 'PBL_RECT', 'PBL_MICROPHONE', 'PBL_SMARTSTRAP', 'PBL_HEALTH', 'PBL_COMPASS', 'PBL_SMARTSTRAP_POWER', 'PBL_DISPLAY_WIDTH=144', 'PBL_DISPLAY_HEIGHT=168', 'PBL_SDK_3']
DEFINES_ST = '-D%s'
DEST_BINFMT = 'elf'
DEST_CPU = 'arm'
DEST_OS = 'linux'
INCLUDES = ['basalt']
LD = 'arm-none-eabi-ld'
LIBDIR = '/usr/local/lib'
LIBPATH_ST = '-L%s'
LIB_DIR = 'node_modules'
LIB_ST = '-l%s'
LINKFLAGS = ['-mcpu=cortex-m3', '-mthumb', '-Wl,--gc-sections', '-Wl,--warn-common', '-fPIE', '-Os']
LINKFLAGS_MACBUNDLE = ['-bundle', '-undefined', 'dynamic_lookup']
LINKFLAGS_cshlib = ['-shared']
LINKFLAGS_cstlib = ['-Wl,-Bstatic']
LINK_CC = ['arm-none-eabi-gcc']
MESSAGE_KEYS = {}
MESSAGE_KEYS_HEADER = '/root/hello-pebblejs/pebble-World-Cup/build/include/message_keys.auto.h'
NODE_PATH = '/root/.pebble-sdk/SDKs/current/node_modules'
PEBBLE_SDK_COMMON = '/root/.pebble-sdk/SDKs/current/sdk-core/pebble/common'
PEBBLE_SDK_PLATFORM = '/root/.pebble-sdk/SDKs/current/sdk-core/pebble/basalt'
PEBBLE_SDK_ROOT = '/root/.pebble-sdk/SDKs/current/sdk-core/pebble'
PLATFORM = {'TAGS': ['basalt', 'color', 'rect', 'mic', 'strap', 'strappower', 'compass', 'health', '144w', '168h'], 'MAX_FONT_GLYPH_SIZE': 256, 'ADDITIONAL_TEXT_LINES_FOR_PEBBLE_H': [], 'MAX_APP_BINARY_SIZE': 65536, 'MAX_RESOURCES_SIZE': 1048576, 'MAX_APP_MEMORY_SIZE': 65536, 'MAX_WORKER_MEMORY_SIZE': 10240, 'NAME': 'basalt', 'BUNDLE_BIN_DIR': 'basalt', 'BUILD_DIR': 'basalt', 'MAX_RESOURCES_SIZE_APPSTORE': 262144, 'DEFINES': ['PBL_PLATFORM_BASALT', 'PBL_COLOR', 'PBL_RECT', 'PBL_MICROPHONE', 'PBL_SMARTSTRAP', 'PBL_HEALTH', 'PBL_COMPASS', 'PBL_SMARTSTRAP_POWER', 'PBL_DISPLAY_WIDTH=144', 'PBL_DISPLAY_HEIGHT=168']}
PLATFORM_NAME = 'basalt'
PREFIX = '/usr/local'
PROJECT_INFO = {u'sdkVersion': u'3', u'uuid': u'133215f0-cf20-4c05-997b-3c9be5a64e5b', u'appKeys': {}, u'companyName': u'Araulin', 'messageKeys': {}, u'targetPlatforms': [u'aplite', u'basalt', u'chalk', u'diorite', u'emery'], u'capabilities': [u'configurable'], u'versionLabel': u'0.4', u'longName': u'World Cup', u'versionCode': 1, u'shortName': u'World Cup', u'watchapp': {u'watchface': False}, u'resources': {u'media': [{u'menuIcon': True, u'type': u'bitmap', u'name': u'IMAGE_MENU_ICON', u'file': u'images/menu_icon.png'}, {u'type': u'bitmap', u'name': u'IMAGE_CUP', u'file': u'images/cup.png'}, {u'type': u'font', u'name': u'SANS_50', u'file': u'fonts/OpenSans.ttf'}]}}
REQUESTED_PLATFORMS = [u'aplite', u'basalt', u'chalk', u'diorite', u'emery']
RESOURCES_JSON = [{u'menuIcon': True, u'type': u'bitmap', u'name': u'IMAGE_MENU_ICON', u'file': u'images/menu_icon.png'}, {u'type': u'bitmap', u'name': u'IMAGE_CUP', u'file': u'images/cup.png'}, {u'type': u'font', u'name': u'SANS_50', u'file': u'fonts/OpenSans.ttf'}]
RPATH_ST = '-Wl,-rpath,%s'
SANDBOX = False
SDK_VERSION_MAJOR = 5
SDK_VERSION_MINOR = 86
SHLIB_MARKER = None
SIZE = 'arm-none-eabi-size'
SONAME_ST = '-Wl,-h,%s'
STLIBPATH_ST = '-L%s'
STLIB_MARKER = None
STLIB_ST = '-l%s'
SUPPORTED_PLATFORMS = ['aplite', 'basalt', 'chalk', 'diorite', 'emery']
TARGET_PLATFORMS = ['emery', 'diorite', 'chalk', 'basalt', 'aplite']
TIMESTAMP = 1530641517
USE_GROUPS = True
VERBOSE = 0
WEBPACK = '/root/.pebble-sdk/SDKs/current/node_modules/.bin/webpack'
cprogram_PATTERN = '%s'
cshlib_PATTERN = 'lib%s.so'
cstlib_PATTERN = 'lib%s.a'
macbundle_PATTERN = '%s.bundle'
