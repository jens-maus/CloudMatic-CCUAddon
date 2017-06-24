#!/bin/tclsh

package require HomeMatic


set dienstngx unknown
set content [::HomeMatic::Util::LoadFile "/etc/config/addons/mh/dienstngx"]
catch { [regexp -line {(.*)} $content dummy dienstngx] }

if {$dienstngx == 1} {
	if {[catch {exec /bin/sh /etc/config/addons/mh/dienstausngx.sh } result]} {
		# non-zero exit status, get it:
		set status [lindex $errorCode 2]
	} else {
		# exit status was 0
		# result contains the result of your command
		set status 0
	}
	if {[catch {exec /bin/sh /etc/config/addons/mh/loophammer.sh } result]} {
		# non-zero exit status, get it:
		set status [lindex $errorCode 2]
	} else {
		# exit status was 0
		# result contains the result of your command
		set status 0
	}
	puts "Der Reverse Proxy Dienst wurde beendet."
}
if {$dienstngx == 0} {
  puts "Der Reverse Proxy Dienst ist bereits deaktiviert."
}