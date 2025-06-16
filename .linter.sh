#!/bin/bash
cd /home/kavia/workspace/code-generation/mockui-match-109711-8ec309c3/mockui_match
npm run build
EXIT_CODE=$?
if [ $EXIT_CODE -ne 0 ]; then
   exit 1
fi

