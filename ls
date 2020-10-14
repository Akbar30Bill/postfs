#!/bin/sh
psql -d postfs -c "select * from \"$POSTFSPWD\""
