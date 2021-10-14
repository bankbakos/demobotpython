#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "6b312792-8502-478b-91b3-4e9e6f74cd10")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "VrQnt5XJ9nF5")
