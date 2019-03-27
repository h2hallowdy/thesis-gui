# THIS IS GUI FOR THESIS
This gui is written by python... 

## Program information
Name:             Testing the tool

Purpose:          Label object bboxes for ImageNet Detection data

Author:           Nguyen, Xuan Hoang

Created:          Thursday Feb 7

Tools:            Python, pyqt, qtDesigner


## HOW TO USE?
    1. Clone the repo or download it from: https://github.com/h2hallowdy/thesis-gui.git

    2. Move to your file dir of this repo.

    3. Images file will be in the "Images" folder: named by number "%3d"( Eg: 001, 002...)

    4. AnnotationsXML and Labels will be auto created after creating Images folder.

    5. Cmd ( or terminal) run: "python main.py".

## NOTE:

    If you cannot run the program, maybe your pc is not installed these python packages yet, please install 

    all the thing in the "import" line by pip. :)


## UI in main GUI
    statusGB: status group box -> sttLbl: status label, configBtn: Configuration Button
    calibGB: calibration group box -> armHomeBtn, camHomeBtn, armTestBtn, camTeachBtn
    armPosGB: arm position group box -> xCurLbl, yCurLbl, zCurLbl
    proPosGB: product position group box -> xProLbl, yProLbl
    controlGB: control group box -> autoBtn, manualBtn
    processGB: process Group box -> processImgFrame
    liveVidGB: live Cam group box -> liveVidFrame

## UI in Configuration GUI
    confiGB: Configuration Group box -> nameCb, baudCb, dataSizeCb, parityCb, handshakeCb, modeCb, openBtn, closeBtn

## UI in ManualMode GUI
    Send angles of motors to test them. :)
