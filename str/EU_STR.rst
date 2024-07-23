.. create pdf with "rst2pdf EU_STR.rst -s styles/str.yaml,styles/cui.yaml --use-floating-images -o EU_STD.pdf"

.. class:: title-logobox

.. list-table::
   :widths: 72

   * - |
       |
       |
       | |ACME_logo|

.. |ACME_logo| image:: images/acme.png
   :width: 245
   :height: 84
   :scale: 250

|
|
|
|

.. class:: title-deepbox

.. list-table::
   :widths: 72

   * - .. class:: title-name

       Software Version Description for Advanced ACME Web Services Appliance
   * - .. class:: title-name

       Engineering Evaluation Unit

|
|
|

.. class:: title-info

Doc Number ACME0081440A

.. class:: title-info

Doc Version 0.1

.. class:: title-info

07/23/24

|
|
|

.. role:: redtext

.. class:: title-deepbox

.. list-table::
   :widths: 72

   * - .. class:: title-notice

        :redtext:`Example Template Text Only`

        Distribution Statement A: Approved for public release. Distribution is unlimited.

        Controlled by: Department of Good Works, Security and Inspection Division, 800-NOT-REAL.

.. contents:: Table of Contents

.. raw:: pdf

   PageBreak

Revisions
=========

Document revision history.

.. list-table::
   :widths: 9 19 11 33
   :header-rows: 1

   * - Revision
     - Author
     - Date
     - Description
   * - 0.1
     - SLA
     - 2024-07-23
     - Initial draft shell


.. raw:: pdf

   PageBreak



1.0 - Scope
===========


1.1 - Identification
~~~~~~~~~~~~~~~~~~~~

This document is the Draft Software Version Description (see revision table)
for the End-user Management Component of the Advanced ACME Web Services Appliance,
Engineering Evaluation Unit.


1.2 - System Overview
~~~~~~~~~~~~~~~~~~~~~

The Advanced ACME Web Services Appliance is an on-premise virtual Web Services
cluster with an advanced management interface.  This document provides both the
Test Description and Test Procedures (steps) for the Management Console only. The
ACME Web Service high-level system components are shown in Figure 1 below:

.. figure:: images/advanced_acme_web_service.png
   :width: 90%

   Figure 1. Advanced ACME Web Service Components

The management console consumes monitoring data and summarizes/displays the
analytics from Spark.


1.3 - Document Overview
~~~~~~~~~~~~~~~~~~~~~~~

The purpose of this STD is to describe the test preparations, test
cases, and test procedures to be used to perform qualification testing
of the Advanced ACME Web Services Appliance management interface. The
content and format generally follow the STD Data Item Description
(DI-IPSC-81439) but includes only the relevant information for an
engineering evaluation unit.

2.0 Referenced documents
========================

:ACME0081439A: `Software Test Description`_ for the Advanced ACME Web Services Appliance
  Engineering Evaluation Unit, revision 0.0.1, 2024-07-23 [ACME0081439A]_
:ACME0081443A: `Software User Manual`_ for the Advanced ACME Web Services Appliance
  Engineering Evaluation Unit, revision 0.0.1, 2023-01-31 [ACME0081443A]_

.. [ACME0081439A]
.. [ACME0081443A]

.. _Software Test Description: https://github.com/VCTLabs/software_test_description_template/blob/master/std/EU_STD.rst
.. _Software User Manual: https://github.com/VCTLabs/software_user_manual_template/blob/master/sum/EU_SUM.rst


3.0 Overview of test results
============================

This section is divided into the following paragraphs. Safety
precautions, marked by WARNING or CAUTION, and security and privacy
considerations are included where applicable.

3.1 Overall assessment of the software tested
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This paragraph shall:

a. Provide an overall assessment of the software as demonstrated by the test results in this report
b. Identify any remaining deficiencies, limitations, or constraints that were detected by the
   testing performed. Problem/change reports may be used to provide deficiency information.
c. For each remaining deficiency, limitation, or constraint, describe:

     1) Its impact on software and system performance, including identification of requirements not met
     2) The impact on software and system design to correct it
     3) A recommended solution/approach for correcting it

3.2 Impact of test environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This paragraph shall provide an assessment of the manner in which the
test environment may be different from the operational environment and
the effect of this difference on the test results.

3.3 Recommended improvements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This paragraph shall provide any recommended improvements in the
design, operation, or testing of the software tested. A discussion of
each recommendation and its impact on the software may be provided. If
no recommended improve- ments are provided, this paragraph shall state
"None."

4.0 Detailed test results
=========================

This section shall be divided into the following paragraphs to describe
the detailed results for each test. Note: The word "test" means a
related collection of test cases.

4.x (Project-unique identifier of a test)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This paragraph shall identify a test by project-unique identifier and
shall be divided into the following subparagraphs to describe the test
results.

4.x.1 Summary of test results
-----------------------------

This paragraph shall summarize the results of the test. The summary
shall include, possibly in a table, the completion status of each test
case associated with the test (for example, "all results as expected,"
"problems encountered," "deviations required"). When the completion
status is not "as expected," this paragraph shall reference the
following paragraphs for details.

4.x.2 Problems encountered
--------------------------

This paragraph shall be divided into subparagraphs that identify
each test case in which one or more problems occurred.

4.x.2.y (Project-unique identifier of a test case)
##################################################

This paragraph shall identify by project-unique identifier a test case
in which one or more problems occurred, and shall provide:

a. A brief description of the problem(s) that occurred
b. Identification of the test procedure step(s) in which they occurred
c. Reference(s) to the associated problem/change report(s) and backup data, as applicable
d. The number of times the procedure or step was repeated in attempting to correct the
   problem(s) and the outcome of each attempt
e. Back-up points or test steps where tests were resumed for retesting

4.x.3 Deviations from test cases/procedures
-------------------------------------------

This paragraph shall be divided into subpara- graphs that identify each
test case in which deviations from test case/test procedures occurred.

4.x.3.y (Project-unique identifier of a test case)
##################################################

This paragraph shall identify by project-unique identifier a test case
in which one or more deviations occurred, and shall provide:

a. A description of the deviation(s) (for example, test case run in which the deviation
   occurred and nature of the deviation, such as substitution of required equipment,
   procedural steps not followed, schedule deviations). (Red-lined test procedures may be
   used to show the deviations)
b. The rationale for the deviation(s)
c. An assessment of the deviations’ impact on the validity of the test case

5.0 Test log
============

This section shall present, possibly in a figure or appendix, a chronological record
of the test events covered by this report. This test log shall include:

a. The date(s), time(s), and location(s) of the tests performed
b. The hardware and software configurations used for each test including, as applicable,
   part/model/serial number, manufacturer, revision level, and calibration date of all
   hardware, and version number and name for the software components used
c. The date and time of each test-related activity, the identity of the individual(s) who
   performed the activity, and the identities of witnesses, as applicable

6.0 Notes
=========

This section shall contain any general information that aids in understanding this
document (e.g., background information, glossary, rationale). This section shall include an
alphabetical listing of all acronyms, abbreviations, and their meanings as used in this document
and a list of any terms and definitions needed to understand this document.


Appendix A. Acronyms and abbreviations
======================================

The following may be used in this document to describe specific technologies
or engineering processes.

:AES: Advanced Encryption Standard - algorithm for symmetric key encryption/decryption
:BIF: Boot Image Format
:CI/CD: Continuous Integration/Continuous Deployment
:CONOPS: Concept of Operations
:COTS: Commercial-Off-The-Shelf
:CSCI: Computer Software Configuration Item
:DT&E: Developmental Test and Evaluation
:FPGA: Field-programmable gate array
:FSBL: First-stage boot loader
:FW: Firmware
:HMAC: Hashed Message Authentication Code - algorithm for private key authentication
:HW: Hardware
:ID: Project-unique identifier
:IRS: Interface Requirements Specification
:ICD: Interface Control Document (should reference IRS docs)
:JTAG: Joint Test Action Group debugging interface
:KPP: Key Performance Parameter
:KSA: Key System Attribute
:LRU: Line-Replaceable Unit
:MOE: Measure of Effectiveness
:MOP: Measure of Performance
:MS: Milestone
:NVM: Nonvolatile Memory
:O&M: Operations and Maintenance
:OCM: On-chip memory
:OT&E: Operational Test and Evaluation
:PL: Programmable Logic - FPGA plus FW
:POR: Power On / Reset
:PS: Processing System - ARMv7 Linux runtime
:PR: Pull Request (agile code review/quality check workflow step)
:R&R: Remove and Replace
:RAM: Reliability, Availability, and Maintainability (aka RMA)
:RC: Release Candidate (SW and FW)
:SS/SRS: System/Subsystem/Software Requirements Specifications
:SS/SDD: System/Subsystem/Software Design Descriptions
:SDP: Software Development Plan
:STP: Software Test Plan
:STR: Software Test Description
:STR: Software Test Report
:SUT: System Under Test
:SW: Software
:T&E: Test and Evaluation
:TDP: Technical Data Package
:VMP: Vulnerability Management Process
