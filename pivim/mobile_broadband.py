"""Module for programatically extracting data from ZTE USB Modems.

These devices incorporate an internal web user interface for checking device statistics
and performing basic functions. In turn, the web user interface accesses
data via an API. However it's possible to call the API directly from code
to get the same data. This module has been tested against the ZTE MF730
(3G) device on the 3 network. It may also work with the ZTE MF823 (4G)
device but this has not been tested.
"""
import logging
import json
import requests

logging.getLogger("requests").setLevel(logging.WARNING)

class MobileBroadband:
    """Class for working with ZTE USB Modems"""
    host = '192.168.0.1'
    url = 'http://{}/goform/goform_get_cmd_process'.format(host)
    hdrs = {'Referer': 'http://{}/'.format(host)}

    def __init__(self):
        self.signalbar = ""
        self.network_type = ""
        self.network_provider = ""

    def get_status(self):
        """
        Returns the current values of the attributes specified in the query string.
        Includes a dummy data set to ensure values are returned where it's
        not possible to work with the USB modem connected.
        """
        if MobileBroadband.is_connected():

            # Query string doesn't work if the cmd is split in to shorter chunks using \
            query_string = {'multi_data': 1,
                            'isTest': 'false',
                            'sms_received_flag_flag': 0,
                            'sts_received_flag_flag': 0,
                            'cmd': 'modem_main_state,pin_status,loginfo,new_version_state,current_upgrade_state,is_mandatory,sms_received_flag,sts_received_flag,signalbar,network_type,network_provider,ppp_status,EX_SSID1,sta_ip_status,EX_wifi_profile,m_ssid_enable,sms_unread_num,RadioOff,simcard_roam,lan_ipaddr,station_mac,battery_charging,battery_vol_percent,battery_pers,spn_display_flag,plmn_display_flag,spn_name_data,spn_b1_flag,spn_b2_flag,realtime_tx_bytes,realtime_rx_bytes,realtime_time,realtime_tx_thrpt,realtime_rx_thrpt,monthly_rx_bytes,monthly_tx_bytes,monthly_time,date_month,data_volume_limit_switch,data_volume_limit_size,data_volume_alert_percent,data_volume_limit_unit,roam_setting_option,upg_roam_switch'} # pylint: disable=line-too-long

            req = requests.get(MobileBroadband.url, params=query_string, \
                headers=MobileBroadband.hdrs)
            res = json.loads(req.text, strict=False)

        else:
            res = {"modem_main_state":"modem_init_complete", "pin_status":"0", \
                "loginfo":"ok", "new_version_state":"version_idle", \
                "current_upgrade_state":"fota_idle", "is_mandatory":"", \
                "sms_received_flag":"", "sts_received_flag":"", \
                "signalbar":"2", "network_type":"DC-HSPA+", \
                "network_provider":"3", "ppp_status":"ppp_connected", \
                "EX_SSID1":"", "sta_ip_status":"", "EX_wifi_profile":"", \
                "m_ssid_enable":"", "sms_unread_num":"0", "sms_dev_unread_num":"0", \
                "sms_sim_unread_num":"0", "RadioOff":"1", \
                "simcard_roam":"Home", "lan_ipaddr":"192.168.0.1", "station_mac":"", \
                "battery_charging":"", "battery_vol_percent":"", \
                "battery_pers":"", "spn_display_flag":"0", "plmn_display_flag":"1", \
                "spn_name_data":"0033", "spn_b1_flag":"0", \
                "spn_b2_flag":"0", "realtime_tx_bytes":"240692", \
                "realtime_rx_bytes":"1265438", "realtime_time":"771", \
                "realtime_tx_thrpt":"69", "realtime_rx_thrpt":"69", \
                "monthly_rx_bytes":"39886898", "monthly_tx_bytes":"2365084", \
                "monthly_time":"14028", "date_month":"201705", \
                "data_volume_limit_switch":"0", "data_volume_limit_size":"", \
                "data_volume_alert_percent":"", "data_volume_limit_unit":"", \
                "roam_setting_option":"off", "upg_roam_switch":"0"}

        self.signalbar = res["signalbar"]
        self.network_type = res["network_type"]
        self.network_provider = res["network_provider"]

    @staticmethod
    def is_connected():
        """
        Determines if the mobile data dongle is connected and functioning correctly
        by checking for the existence of the web portal.
        """

        try:
            # Requests throws an exception if a site doesn't exist
            req = requests.head("http://m.home") # pylint: disable=unused-variable
            return True
        except requests.ConnectionError:
            return False
