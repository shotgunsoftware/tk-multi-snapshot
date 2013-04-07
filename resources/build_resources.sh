#!/usr/bin/env bash
# 
# Copyright (c) 2008 Shotgun Software, Inc
# ----------------------------------------------------

echo "building user interfaces..."
pyside-uic --from-imports snapshot_form.ui > ../python/tk_multi_snapshot/ui/snapshot_form.py
pyside-uic --from-imports snapshot_history_form.ui > ../python/tk_multi_snapshot/ui/snapshot_history_form.py

echo "building resources..."
pyside-rcc resources.qrc > ../python/tk_multi_snapshot/ui/resources_rc.py
