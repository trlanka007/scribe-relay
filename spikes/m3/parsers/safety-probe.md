# Extended synthetic safety and reconciliation probe

Refs #91 #92. Run `python safety_probe.py` from this directory (standard library only). Eleven unittest cases cover complex XML inventory, multiset reconciliation, external relationship reporting, URL checks, invalid ZIP, malformed XML, DTD, unsafe path, duplicate entry, oversized part and missing document part.

The fixture deliberately models XML structures rather than a complete Word-authored OPC package. The inventory records path, type and text, including inserted/deleted text, hyperlinks, text boxes, nested tables and merge markers. These are detection records, not a policy for displaying tracked changes. Reconciliation compares multiplicity and content; it does not independently prove semantic order or complete extraction. External relationships are reported, never fetched.

Limitations: the probe is not a production security boundary; it does not cover all OPC relationships, XML encodings, ZIP attacks, resource exhaustion, footnotes, headers, drawing semantics or browser URL interpretation. The exact committed tests have not been executed in this turn; run them before accepting evidence. Do not infer comprehensive DOCX or LinkedIn support. No production dependency changes.
