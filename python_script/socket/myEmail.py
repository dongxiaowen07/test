#!/usr/bin/env python
# coding: utf-8

from smtplib import SMTP
from poplib import POP3
from time import sleep

SMTPSVR='smtp.163.com'
POP3SVR='pop.163.com'

origHdrs = ['From: dongxiaowen07@163.com', 'To: dongxiaowen001@ke.com', 'Subject: test msg']
origBody = ['xxx', 'yyy', 'zzz']
origMsg = '\r\n\r\n'.join(['\r\n'.join(origHdrs), '\r\n'.join(origBody)])

sendSvr = SMTP(SMTPSVR)
sendSvr.login('dongxiaowen07', '1q2w3e4r')
errs = sendSvr.sendmail(
    'dongxiaowen07@163.com',
    ('dongxiaowen001@ke.com',),
    origMsg
)

sendSvr.quit()
assert len(errs) == 0, errs
print 'send email successfully!'
sleep(10)

recvSvr = POP3(POP3SVR)
recvSvr.user('dongxiaowen07')
recvSvr.pass_('1q2w3e4r')
rsp, msg, siz = recvSvr.retr(recvSvr.stat()[0])
sep = msg.index('')
recvBody = msg[sep+1:]
# assert origBody == recvBody
print recvBody
print 'receive emails successfully!'