# -*- coding: utf-8 -*-
#
# Copyright (C) 2010-2016 PPMessage.
# Guijin Ding, dingguijin@gmail.com.
# All rights are reserved.
#
# core/constant.py
#

def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    return type('Enum', (), enums)

Numbers = enum('ZERO', 'ONE', 'TWO')
# Numbers.ZERO == 0 and Numbers.ONE == 1

class Enum(set):
    def __getattr__(self, name):
        if name in self:
            return name
        raise AttributeError

Animals = Enum(["DOG", "CAT", "HORSE"])
# Animals.DOG == "DOG"

RULE_STATUS = Enum([
    "LIVE",
    "PAUSE"
])

DISTRIBUTE_RESULT = Enum([
    "WAITING",
    "SUCCESS",
    "ERROR",
    "USER_NOT_MATCHED",
    "NO_TARGET_SERVICE"
])

CONFIG_STATUS = Enum([
    "NONE",
    "SERVER",
    "DATABASE",
    "FIRST",
    "RESTART"
])

SQL = Enum([
    "NONE",
    "MYSQL",
    "PGSQL",
    "SQLITE",
])

PP_WEB_SERVICE = Enum([
    "META",
    "ABSTRACT",
    "UPLOAD",
    "DOWNLOAD",
    "API",
    "PCSOCKET",
    "PPCOM",
    "PPKEFU",
    "PPCONSOLE",
    "PPAUTH",
    "AMD",
    "CACHE",
    "DISPATCHER",
    "GCMPUSH",
    "IOSPUSH",
    "MQTTPUSH",
    "PPEMAIL",
    "SEND",
    "PPCONFIG",
    "IDENTICON"
])

CACHE_TYPE = Enum([
    "CREATE",
    "UPDATE",
    "DELETE"
])

API_LEVEL = Enum([
    "PPCOM",
    "PPKEFU",
    "PPCONSOLE",
    "PPCONSOLE_BEFORE_LOGIN",
    "THIRD_PARTY_KEFU",
    "THIRD_PARTY_CONSOLE",
])

TRAIN_METHOD = Enum([
    "BAYES",
    "SVM",
    "KNN",
    "SGD",
])

DIS_WHAT = Enum([
    "WS",
    "ACK",
    "MSG",
    "AUTH",
    "SEND",
    "ONLINE",
    "TYPING",
    "TYPING_WATCH",
    "TYPING_UNWATCH",
    "CONVERSATION",
])

ONLINE_STATUS = Enum([
    "OFFLINE",
    "ONLINE",
    "UNCHANGED",
])

USER_ONLINE_STATUS = Enum([
    "OFFLINE",
    "PORTAL_ONLINE_BROWSER",
    "PORTAL_ONLINE_MOBILE",
    "SERVICE_ONLINE_MOBILE",
    "SERVICE_ONLINE_BROWSER",
    "SERVICE_ONLINE_PC",
    "SERVICE_ONLINE_MOBILE_PC",
    "SERVICE_ONLINE_MOBILE_BROWSER"
])

WEBSOCKET_STATUS = Enum([
    "NULL",
    "OPEN",
    "CLOSE"
])

# OWNER and SERVICE are both PPMESSAGE user
# OWNER_0 is user after signing up
# OWNER_1 is user after creating first app
# OWNER_2 is user after launching team
# owner_3 is ???
# ADMIN is the admin user
# ANONYMOUS is PPMESSAGE anonymous + customer's anonymous
# THIRDPARTY is customer's user
USER_STATUS = Enum([
    "OWNER_0",
    "OWNER_1",
    "OWNER_2",
    "OWNER_3",
    "ADMIN",
    "SERVICE",
    "ANONYMOUS",
    "THIRDPARTY",
])

MQTTPUSH_SRV = Enum([
    "PUSH",
])

GCMPUSH_SRV = Enum([
    "PUSH",
])

IOSPUSH_SRV = Enum([
    "PUSH",
])

PCSOCKET_SRV = Enum([
    "WS",
    "ACK",
    "PUSH",
    "ONLINE",
    "TYPING",
    "LOGOUT",
])

DIS_SRV = Enum([
    "MESSAGE_DIS",
])

CACHE_SRV = Enum([
    "ADD_NO_DB",
    "ADD",
    "UPDATE",
    "DELETE",
    "DELETE_NO_DB",
    "PING",
])

SEND_SRV = Enum([
    "SEND",
])

TASK_STATUS = Enum([
    "PENDING",
    "PROCESSED",
    "CANCELLED",
    "ACKED"
]) 

MESSAGE_STATUS = Enum([
    "PENDING",
    "FAILED",
    "PUSHED",
    "ACKED",
    "NODEVICE"
])

OS = Enum([
    "AND", # ANDROID
    "IOS", # IOS
    "ANB", # ANDROID BROWSER
    "IOB", # IOS BROWSER
    "WIP", # WIN PHONE
    "MAC", # MAC OS X PC
    "LIN", # LINUX PC
    "WIN", # WINDOWS PC
    "MAB", # MAC BROWSER
    "LIB", # LINUX BROWSER
    "WIB", # WINDOWS BROWSER
    "W32", # WINDOWS 32 BIT
    "W64", # WINDOWS 64 BIT
])

MESSAGE_TYPE = Enum([
    "NOTI",
    "ACT",
    "SYS",
])

MESSAGE_SUBTYPE = Enum([
    "TEXT",
    "TXT",
    "IMAGE",
    "AUDIO",
    "VIDEO",
    "DOCUMENT",
    "ARCHIVE",
    "FILE",
    "SINGLE_CARD",
    "MULTIPLE_CARD",
    "EVENT",
    "MENU",
    "FUNC",
    "GPS_LOCATION",
    "DG_INVITED",
    "DG_REMOVED",
    "AG_INVITED",
    "INVITE_CONTACT",
    "ACCEPT_CONTACT",
    "REMOVE_CONTACT",
    "REQUEST_JOIN_OG",
    "APPROVE_JOIN_OG",
    "LOGOUT",
])


YVOBJECT = Enum([
    "DU",
    "OG",
    "AG",
    "AU",
    "DG",
    "CV",
    "AP",
])

CONVERSATION_TYPE = Enum([
    "S2S", # service user to service user
    "S2P", # service user to portal user
    "P2S", # portal user to service user
])

CONVERSATION_STATUS = Enum([
    "NEW",
    "OPEN",
    "CLOSE",
])

CONVERSATION_MEMBER_ACTION = Enum([
    "ADD",
    "REMOVE"
])


APNS_TITLE = {
    "ZH_CN" : {
        "UNKNOWN": "未知类型",
        "TXT": "文本消息",
        "GPS": "位置消息",
        "AUDIO": "语音消息",
        "IMAGE": "图像消息",
        "SINGLE_CARD": "图文消息",
        "MULTIPLE_CARD": "多图文消息",
        "FILE": "文件消息",
        "INVITE": "邀请消息",
        "ACCEPT": "好友邀请通过消息",
        "DG_INVITED": "加入群聊消息"
    },
    
    "EN_US" : {
        "UNKNOWN": "unknown message type",
        "TXT": "text message",
        "GPS": "location message",
        "AUDIO": "voice message",
        "IMAGE": "picture message",
        "SINGLE_CARD": "rich text message",
        "MULTIPLE_CARD": "rich text message",
        "FILE": "file message",
        "INVITE": "invitation message",
        "ACCEPT": "invitation accepted message",
        "DG_INVITED": "discussion group invitation message"
    },
}

THUMBNAIL_WIDTH = 120
THUMBNAIL_HEIGHT = 160

KEYTOOL_PATH = r"keytool -printcert -file"

MESSAGE_MAX_TEXT_LEN = 128
UPLOAD_MAX_BYTE = 20971520 #20M

# 1000ms to check AMD queue
CHECK_AMD_INTERVAL = 1000

# 50ms to check send queue
CHECK_SEND_INTERVAL = 50

MQTT_HOST = "127.0.0.1"
MQTT_PORT = 1883

API_HOST = "127.0.0.1"
API_PORT = 8922

DIS_HOST = "127.0.0.1"
DIS_PORT = 8923

ADMINWEB_PORT = 8920
USERWEB_PORT = 8925

FUNC_HOST = "127.0.0.1"
FUNC_PORT = 8926

PPKEFU_PORT = 8927

FILEDOWNLOAD_PORT = 8924
FILEUPLOAD_PORT = 8928

CACHE_HOST = "127.0.0.1"
CACHE_PORT = 8929

REDIS_HOST = "127.0.0.1"
REDIS_PORT = 6379

OAUTH_HOST = "127.0.0.1"
OAUTH_PORT = 8930

MESSAGE_PORT = 8003

PCSOCKET_HOST = "127.0.0.1"
PCSOCKET_PORT = 8931

IOSPUSH_HOST = "127.0.0.1"
IOSPUSH_PORT = 8932
    
PPCOM_PORT = 8934

PPAUTOINSTALL_PORT = 8936
PPAUTOINSTALL_HOST = "127.0.0.1"

SEND_HOST = "127.0.0.1"
SEND_PORT = 8938

MQTTPUSH_HOST = "127.0.0.1"
MQTTPUSH_PORT = 8939

GCMPUSH_HOST = "127.0.0.1"
GCMPUSH_PORT = 8940

PPAUTH_PORT = 8943

PPCONSOLE_PORT = 8944

# all in one backend service port
MAIN_PORT = 8945

PPCONFIG_PORT = 8946

IDENTICON_PORT = 8947

TORNADO_FILEUPLOAD_PORT = 8948

IOS_FAKE_TOKEN = "YOU-GOT-A-FAKE-IOS-TOKEN-IN-EMULATOR"
INVALID_IOS_TOKEN = "INVALID_IOS_TOKEN"

PPCOM_WELCOME = {
    "en_us": "Any question is welcome. Waiting for you.",
    "zh_cn": "有什么可以帮忙的，一起聊两句吧？",
    "zh_tw": "有什麼可以幫忙的，一起聊兩句吧？",
}

PPCOM_OFFLINE = {
    "en_us": "We are sorry for nobody is online now, but your messages will be delivered and read by customer service when they are online.",
    "zh_cn": "抱歉没有客服人员在线，消息依旧会被投递，客服人员上线的时候能马上看到。",
    "zh_tw": "抱歉沒有客服人員在線，消息依舊會被投遞，客服人員上線的時候能馬上看到。",
}

PPCOM_LAUNCHER_STYLE = Enum([
    "DEFAULT",
    "MATERIAL",
    "ANIMATE",
])

SHOW_PPCOM_HOVER = Enum([
    "NEVER",
    "ALWAYS",
    "ONCE",
])

GROUP_ALGORITHM = Enum([
    "META",
    "ABASTRACT",
    "BROADCAST",
    "SMART",
    "LOAD",
    "ROBOT",
])

SERVICE_USER_STATUS = Enum([
    "NULL",
    "READY",
    "BUSY",
    "REST",
])

USER_NAME = {
    "en": {
        "local": "Local Area",
        "unknown": "Unknown Area",
        "user": "User",
    },

    "cn": {
        "local": "本地",
        "unknown": "未知区域",
        "user": "用户",
    },

    "tw": {
        "local": "本地",
        "unknown": "未知區域",
        "user": "用戶",
    },
}

# email key is a list which queue all email sending request
REDIS_EMAIL_KEY = "redis_email_key"

# iospush key is a list which queue all ios push request
REDIS_JPUSH_KEY = "redis_jpush_key"
REDIS_IOSPUSH_KEY = "redis_iospush_key"
REDIS_GCMPUSH_KEY = "redis_gcmpush_key"
REDIS_MQTTPUSH_KEY = "redis_mqttpush_key"

REDIS_TYPING_LISTEN_KEY = "redis_typing_listen_key"
REDIS_ONLINE_LISTEN_KEY = "redis_online_listen_key"

REDIS_ACK_NOTIFICATION_KEY = "redis_ack_notification_key"
REDIS_PUSH_NOTIFICATION_KEY = "redis_push_notification_key"
REDIS_SEND_NOTIFICATION_KEY = "redis_send_notification_key"
REDIS_TYPING_NOTIFICATION_KEY = "redis_typing_notification_key"
REDIS_ONLINE_NOTIFICATION_KEY = "redis_online_notification_key"
REDIS_LOGOUT_NOTIFICATION_KEY = "redis_logout_notification_key"
REDIS_DISPATCHER_NOTIFICATION_KEY = "redis_dispatcher_notification_key"

REDIS_AMD_KEY = "redis_amd_key"

REDIS_PPKEFU_ONLINE_KEY = "redis_ppkefu_online_key"
REDIS_PPCOM_ONLINE_KEY = "redis_ppcom_online_key"

REDIS_CACHE_KEY = "redis_cache_key"
REDIS_SEARCH_KEY = "redis_search_key"

DATETIME_FORMAT = {
    "extra": '%Y-%m-%d %H:%M:%S %f',
    "basic": '%Y-%m-%d %H:%M:%S'
}
