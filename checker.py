import base64
def stringToBase64(s):
    return base64.b64encode(s.encode('latin-1'))

def base64ToString(b):
    return base64.b64decode(b).decode('latin-1')

ans = base64ToString("eyAiYWNoaWV2ZW1lbnRzIjogeyAicGF5VG9XaW4iOiB7ICJ1bmxvY2tlZCI6IGZhbHNlLCAiZmxhZ3MiOiB7IH0gfSwgInRpbWVUb1VwZ3JhZGUiOiB7ICJ1bmxvY2tlZCI6IGZhbHNlLCAiZmxhZ3MiOiB7IH0gfSwgInRoYW5rWW91IjogeyAidW5sb2NrZWQiOiBmYWxzZSwgImZsYWdzIjogeyB9IH0sICJwYWNpZmlzdCI6IHsgInVubG9ja2VkIjogZmFsc2UsICJmbGFncyI6IHsgfSB9LCAic2FmZUlTd2VhciI6IHsgInVubG9ja2VkIjogZmFsc2UsICJmbGFncyI6IHsgfSB9LCAiZ3VyYUdhY2hpa29pIjogeyAidW5sb2NrZWQiOiBmYWxzZSwgImZsYWdzIjogeyB9IH0sICJheWFtZUdhY2hpa29pIjogeyAidW5sb2NrZWQiOiBmYWxzZSwgImZsYWdzIjogeyB9IH0sICJrb3JvbmUxMCI6IHsgInVubG9ja2VkIjogZmFsc2UsICJmbGFncyI6IHsgfSB9LCAiZmlyc3Rib3NzIjogeyAidW5sb2NrZWQiOiBmYWxzZSwgImZsYWdzIjogeyB9IH0sICJzdWlzZWlHYWNoaWtvaSI6IHsgInVubG9ja2VkIjogZmFsc2UsICJmbGFncyI6IHsgfSB9LCAiZnVsbENvbGxhYiI6IHsgInVubG9ja2VkIjogZmFsc2UsICJmbGFncyI6IHsgfSB9LCAibWF0c3VyaUdhY2hpa29pIjogeyAidW5sb2NrZWQiOiBmYWxzZSwgImZsYWdzIjogeyB9IH0sICJrcm9uaWlHYWNoaWtvaSI6IHsgInVubG9ja2VkIjogZmFsc2UsICJmbGFncyI6IHsgfSB9LCAianVzdFJORyI6IHsgInVubG9ja2VkIjogZmFsc2UsICJmbGFncyI6IHsgfSB9LCAiaWRvbGdyb3VwIjogeyAidW5sb2NrZWQiOiBmYWxzZSwgImZsYWdzIjogeyB9IH0sICJpcnlzQ2xlYXIiOiB7ICJ1bmxvY2tlZCI6IGZhbHNlLCAiZmxhZ3MiOiB7IH0gfSwgInNvcmFDbGVhciI6IHsgInVubG9ja2VkIjogZmFsc2UsICJmbGFncyI6IHsgfSB9LCAia29yb25lQ2xlYXIiOiB7ICJ1bmxvY2tlZCI6IGZhbHNlLCAiZmxhZ3MiOiB7IH0gfSwgImlyeXNHYWNoaWtvaSI6IHsgInVubG9ja2VkIjogZmFsc2UsICJmbGFncyI6IHsgfSB9LCAiQ0VPbm93IjogeyAidW5sb2NrZWQiOiBmYWxzZSwgImZsYWdzIjogeyB9IH0sICJpRGlkSXQiOiB7ICJ1bmxvY2tlZCI6IGZhbHNlLCAiZmxhZ3MiOiB7IH0gfSwgImZpcmVkIjogeyAidW5sb2NrZWQiOiBmYWxzZSwgImZsYWdzIjogeyB9IH0sICJraWFyYUNsZWFyIjogeyAidW5sb2NrZWQiOiBmYWxzZSwgImZsYWdzIjogeyB9IH0sICJmdWJ1a2lDbGVhciI6IHsgInVubG9ja2VkIjogZmFsc2UsICJmbGFncyI6IHsgfSB9LCAiYWtpQ2xlYXIiOiB7ICJ1bmxvY2tlZCI6IGZhbHNlLCAiZmxhZ3MiOiB7IH0gfSwgImFxdWFDbGVhciI6IHsgInVubG9ja2VkIjogZmFsc2UsICJmbGFncyI6IHsgfSB9LCAiNTBoYW1idXJnZXJzIjogeyAidW5sb2NrZWQiOiBmYWxzZSwgImZsYWdzIjogeyB9IH0sICJjaG9jb0NsZWFyIjogeyAidW5sb2NrZWQiOiBmYWxzZSwgImZsYWdzIjogeyB9IH0sICJ0cnVlUk5HIjogeyAidW5sb2NrZWQiOiBmYWxzZSwgImZsYWdzIjogeyB9IH0sICJhemtpQ2xlYXIiOiB7ICJ1bmxvY2tlZCI6IGZhbHNlLCAiZmxhZ3MiOiB7IH0gfSwgInBheURheSI6IHsgInVubG9ja2VkIjogZmFsc2UsICJmbGFncyI6IHsgfSB9LCAiYW1lQ2xlYXIiOiB7ICJ1bmxvY2tlZCI6IGZhbHNlLCAiZmxhZ3MiOiB7IH0gfSwgImNhbGxpMTAiOiB7ICJ1bmxvY2tlZCI6IGZhbHNlLCAiZmxhZ3MiOiB7IH0gfSwgImJhZUNsZWFyIjogeyAidW5sb2NrZWQiOiBmYWxzZSwgImZsYWdzIjogeyB9IH0sICJzb3JhR2FjaGlrb2kiOiB7ICJ1bmxvY2tlZCI6IGZhbHNlLCAiZmxhZ3MiOiB7IH0gfSwgInNvbG9CZWF0ZXIiOiB7ICJ1bmxvY2tlZCI6IGZhbHNlLCAiZmxhZ3MiOiB7IH0gfSwgInBvd2VyTGV2ZWxsaW5nIjogeyAidW5sb2NrZWQiOiBmYWxzZSwgImZsYWdzIjogeyB9IH0sICJtaWtvQ2xlYXIiOiB7ICJ1bmxvY2tlZCI6IGZhbHNlLCAiZmxhZ3MiOiB7IH0gfSwgImtpYXJhR2FjaGlrb2kiOiB7ICJ1bmxvY2tlZCI6IGZhbHNlLCAiZmxhZ3MiOiB7IH0gfSwgImxvb2tJbU9uVFYiOiB7ICJ1bmxvY2tlZCI6IGZhbHNlLCAiZmxhZ3MiOiB7IH0gfSwgImhhYXRvQ2xlYXIiOiB7ICJ1bmxvY2tlZCI6IGZhbHNlLCAiZmxhZ3MiOiB7IH0gfSwgInRvb2hhbHUiOiB7ICJ1bmxvY2tlZCI6IGZhbHNlLCAiZmxhZ3MiOiB7IH0gfSwgImFxdWFHYWNoaWtvaSI6IHsgInVubG9ja2VkIjogZmFsc2UsICJmbGFncyI6IHsgfSB9LCAic2Vjb25kYm9zcyI6IHsgInVubG9ja2VkIjogZmFsc2UsICJmbGFncyI6IHsgfSB9LCAicGV0RG9nIjogeyAidW5sb2NrZWQiOiBmYWxzZSwgImZsYWdzIjogeyB9IH0sICJtdXNjbGUiOiB7ICJ1bmxvY2tlZCI6IGZhbHNlLCAiZmxhZ3MiOiB7IH0gfSwgImFtZUdhY2hpa29pIjogeyAidW5sb2NrZWQiOiBmYWxzZSwgImZsYWdzIjogeyB9IH0sICJkZWx1c2lvbmFsIjogeyAidW5sb2NrZWQiOiBmYWxzZSwgImZsYWdzIjogeyB9IH0sICJrcm9uaWlDbGVhciI6IHsgInVubG9ja2VkIjogZmFsc2UsICJmbGFncyI6IHsgfSB9LCAiZ3JpbmQiOiB7ICJ1bmxvY2tlZCI6IGZhbHNlLCAiZmxhZ3MiOiB7IH0gfSwgImJhZUdhY2hpa29pIjogeyAidW5sb2NrZWQiOiBmYWxzZSwgImZsYWdzIjogeyB9IH0sICJTQ1QiOiB7ICJ1bmxvY2tlZCI6IGZhbHNlLCAiZmxhZ3MiOiB7IH0gfSwgImJvaW5nIjogeyAidW5sb2NrZWQiOiBmYWxzZSwgImZsYWdzIjogeyB9IH0sICIxaGFyZCI6IHsgInVubG9ja2VkIjogZmFsc2UsICJmbGFncyI6IHsgfSB9LCAiMmhhcmQiOiB7ICJ1bmxvY2tlZCI6IGZhbHNlLCAiZmxhZ3MiOiB7IH0gfSwgInlhZ29vc3RhdHVlIjogeyAidW5sb2NrZWQiOiBmYWxzZSwgImZsYWdzIjogeyB9IH0sICJkb250RmFpbCI6IHsgInVubG9ja2VkIjogZmFsc2UsICJmbGFncyI6IHsgfSB9LCAiZnJlZVN0aWNrZXJzIjogeyAidW5sb2NrZWQiOiBmYWxzZSwgImZsYWdzIjogeyB9IH0sICJtdW1laUNsZWFyIjogeyAidW5sb2NrZWQiOiBmYWxzZSwgImZsYWdzIjogeyB9IH0sICJtaW9DbGVhciI6IHsgInVubG9ja2VkIjogZmFsc2UsICJmbGFncyI6IHsgfSB9LCAiaGFyZGNvcmVHYW1lciI6IHsgInVubG9ja2VkIjogZmFsc2UsICJmbGFncyI6IHsgfSB9LCAiYWxsY29tcGxldGUiOiB7ICJ1bmxvY2tlZCI6IGZhbHNlLCAiZmxhZ3MiOiB7IH0gfSwgIm9rYXl1R2FjaGlrb2kiOiB7ICJ1bmxvY2tlZCI6IGZhbHNlLCAiZmxhZ3MiOiB7IH0gfSwgInRoaXJkYm9zcyI6IHsgInVubG9ja2VkIjogZmFsc2UsICJmbGFncyI6IHsgfSB9LCAicm9ib2NvQ2xlYXIiOiB7ICJ1bmxvY2tlZCI6IGZhbHNlLCAiZmxhZ3MiOiB7IH0gfSwgIm9ibGl0ZXJhdGVkIjogeyAidW5sb2NrZWQiOiBmYWxzZSwgImZsYWdzIjogeyB9IH0sICJub3RUYWtpbmdBbnlDaGFuY2VzIjogeyAidW5sb2NrZWQiOiBmYWxzZSwgImZsYWdzIjogeyB9IH0sICJiYWUxMCI6IHsgInVubG9ja2VkIjogZmFsc2UsICJmbGFncyI6IHsgfSB9LCAiaW5hQ2xlYXIiOiB7ICJ1bmxvY2tlZCI6IGZhbHNlLCAiZmxhZ3MiOiB7IH0gfSwgInNhbmFDbGVhciI6IHsgInVubG9ja2VkIjogZmFsc2UsICJmbGFncyI6IHsgfSB9LCAiZmF1bmFDbGVhciI6IHsgInVubG9ja2VkIjogZmFsc2UsICJmbGFncyI6IHsgfSB9LCAic3BlZWRydW5uZXIiOiB7ICJ1bmxvY2tlZCI6IGZhbHNlLCAiZmxhZ3MiOiB7IH0gfSwgImZpcnN0Y2xlYXIiOiB7ICJ1bmxvY2tlZCI6IGZhbHNlLCAiZmxhZ3MiOiB7IH0gfSwgInNoaW9uQ2xlYXIiOiB7ICJ1bmxvY2tlZCI6IGZhbHNlLCAiZmxhZ3MiOiB7IH0gfSwgIm9rYXl1Q2xlYXIiOiB7ICJ1bmxvY2tlZCI6IGZhbHNlLCAiZmxhZ3MiOiB7IH0gfSwgImx2NTAiOiB7ICJ1bmxvY2tlZCI6IGZhbHNlLCAiZmxhZ3MiOiB7IH0gfSwgIm1lbENsZWFyIjogeyAidW5sb2NrZWQiOiBmYWxzZSwgImZsYWdzIjogeyB9IH0sICJzdWJhcnVHYWNoaWtvaSI6IHsgInVubG9ja2VkIjogZmFsc2UsICJmbGFncyI6IHsgfSB9LCAic2FuYUdhY2hpa29pIjogeyAidW5sb2NrZWQiOiBmYWxzZSwgImZsYWdzIjogeyB9IH0sICJhemtpR2FjaGlrb2kiOiB7ICJ1bmxvY2tlZCI6IGZhbHNlLCAiZmxhZ3MiOiB7IH0gfSwgImtvcm9uZUdhY2hpa29pIjogeyAidW5sb2NrZWQiOiBmYWxzZSwgImZsYWdzIjogeyB9IH0sICJjaG9jb0dhY2hpa29pIjogeyAidW5sb2NrZWQiOiBmYWxzZSwgImZsYWdzIjogeyB9IH0sICJmbGVzaFdvdW5kIjogeyAidW5sb2NrZWQiOiBmYWxzZSwgImZsYWdzIjogeyB9IH0sICJheWFtZUNsZWFyIjogeyAidW5sb2NrZWQiOiBmYWxzZSwgImZsYWdzIjogeyB9IH0sICJtZWxHYWNoaWtvaSI6IHsgInVubG9ja2VkIjogZmFsc2UsICJmbGFncyI6IHsgfSB9LCAiaW5hR2FjaGlrb2kiOiB7ICJ1bmxvY2tlZCI6IGZhbHNlLCAiZmxhZ3MiOiB7IH0gfSwgImZ1YnVraUdhY2hpa29pIjogeyAidW5sb2NrZWQiOiBmYWxzZSwgImZsYWdzIjogeyB9IH0sICJtdW1laUdhY2hpa29pIjogeyAidW5sb2NrZWQiOiBmYWxzZSwgImZsYWdzIjogeyB9IH0sICJtaWxsaW9uYWlyZSI6IHsgInVubG9ja2VkIjogZmFsc2UsICJmbGFncyI6IHsgfSB9LCAiaW5hMTAiOiB7ICJ1bmxvY2tlZCI6IGZhbHNlLCAiZmxhZ3MiOiB7IH0gfSwgImx2MTAwIjogeyAidW5sb2NrZWQiOiBmYWxzZSwgImZsYWdzIjogeyB9IH0sICIxMDAwMGRhbWFnZSI6IHsgInVubG9ja2VkIjogZmFsc2UsICJmbGFncyI6IHsgfSB9LCAiaGFsbHVjaW5hdGVkIjogeyAidW5sb2NrZWQiOiBmYWxzZSwgImZsYWdzIjogeyB9IH0sICJha2lHYWNoaWtvaSI6IHsgInVubG9ja2VkIjogZmFsc2UsICJmbGFncyI6IHsgfSB9LCAiY2FsbGlHYWNoaWtvaSI6IHsgInVubG9ja2VkIjogZmFsc2UsICJmbGFncyI6IHsgfSB9LCAic3ViYXJ1Q2xlYXIiOiB7ICJ1bmxvY2tlZCI6IGZhbHNlLCAiZmxhZ3MiOiB7IH0gfSwgImx1Y2t5RGF5IjogeyAidW5sb2NrZWQiOiBmYWxzZSwgImZsYWdzIjogeyB9IH0sICJraWFyYTEwIjogeyAidW5sb2NrZWQiOiBmYWxzZSwgImZsYWdzIjogeyB9IH0sICJjb3VjaFBvdGF0byI6IHsgInVubG9ja2VkIjogZmFsc2UsICJmbGFncyI6IHsgfSB9LCAiYnV5aW5nUG93ZXIiOiB7ICJ1bmxvY2tlZCI6IGZhbHNlLCAiZmxhZ3MiOiB7IH0gfSwgInNoaW9uR2FjaGlrb2kiOiB7ICJ1bmxvY2tlZCI6IGZhbHNlLCAiZmxhZ3MiOiB7IH0gfSwgImRvbnROZWVkIjogeyAidW5sb2NrZWQiOiBmYWxzZSwgImZsYWdzIjogeyB9IH0sICJpZG9sUG93ZXIiOiB7ICJ1bmxvY2tlZCI6IGZhbHNlLCAiZmxhZ3MiOiB7IH0gfSwgInNoaW9uMTAiOiB7ICJ1bmxvY2tlZCI6IGZhbHNlLCAiZmxhZ3MiOiB7IH0gfSwgIm1pa29HYWNoaWtvaSI6IHsgInVubG9ja2VkIjogZmFsc2UsICJmbGFncyI6IHsgfSB9LCAiY2FsbGlDbGVhciI6IHsgInVubG9ja2VkIjogZmFsc2UsICJmbGFncyI6IHsgfSB9LCAicGFpblBla28iOiB7ICJ1bmxvY2tlZCI6IGZhbHNlLCAiZmxhZ3MiOiB7IH0gfSwgInJvYm9jb0dhY2hpa29pIjogeyAidW5sb2NrZWQiOiBmYWxzZSwgImZsYWdzIjogeyB9IH0sICJtYXRzdXJpQ2xlYXIiOiB7ICJ1bmxvY2tlZCI6IGZhbHNlLCAiZmxhZ3MiOiB7IH0gfSwgImZ1bGx5TG9hZGVkIjogeyAidW5sb2NrZWQiOiBmYWxzZSwgImZsYWdzIjogeyB9IH0sICJtaWRib3NzIjogeyAidW5sb2NrZWQiOiBmYWxzZSwgImZsYWdzIjogeyB9IH0sICJzdWlzZWlDbGVhciI6IHsgInVubG9ja2VkIjogZmFsc2UsICJmbGFncyI6IHsgfSB9LCAiaXJ5czEwIjogeyAidW5sb2NrZWQiOiBmYWxzZSwgImZsYWdzIjogeyB9IH0sICJoYWF0b0dhY2hpa29pIjogeyAidW5sb2NrZWQiOiBmYWxzZSwgImZsYWdzIjogeyB9IH0sICJzYW5hMTAiOiB7ICJ1bmxvY2tlZCI6IGZhbHNlLCAiZmxhZ3MiOiB7IH0gfSwgImd1cmFDbGVhciI6IHsgInVubG9ja2VkIjogZmFsc2UsICJmbGFncyI6IHsgfSB9LCAibWlvR2FjaGlrb2kiOiB7ICJ1bmxvY2tlZCI6IGZhbHNlLCAiZmxhZ3MiOiB7IH0gfSwgImZhdW5hR2FjaGlrb2kiOiB7ICJ1bmxvY2tlZCI6IGZhbHNlLCAiZmxhZ3MiOiB7IH0gfSwgIjEwMDBkYW1hZ2UiOiB7ICJ1bmxvY2tlZCI6IGZhbHNlLCAiZmxhZ3MiOiB7IH0gfSwgIndhbXkiOiB7ICJ1bmxvY2tlZCI6IGZhbHNlLCAiZmxhZ3MiOiB7IH0gfSB9LCAiZm9vZCI6IDAuMCwgImdyb3d0aCI6IDAuMCwgInNwZWNVbmxvY2siOiAwLjAsICJHUk9mZiI6IDAuMCwgImhhc3RlIjogMC4wLCAiaG9sb0NvaW5zIjogLTIwNy4wLCAibW9iVXAiOiAwLjAsICJ1bmxvY2tlZEl0ZW1zIjogWyAiQm9keVBpbGxvdyIsICJGdWxsTWVhbCIsICJQaWtpUGlraVBpbWFuIiwgIlN1Y2N1YnVzSG9ybiIsICJIZWFkcGhvbmVzIiwgIlViZXJTaGVlcCIsICJIb2x5TWlsayIsICJTYWtlIiwgIkZhY2VNYXNrIiBdLCAidGVhcnMiOiBbIFsgIm15dGgiLCAwLjAgXSwgWyAiY291bmNpbEhvcGUiLCAwLjAgXSwgWyAiZ2FtZXJzIiwgMC4wIF0sIFsgImdlbjAiLCAwLjAgXSwgWyAiZ2VuMSIsIDAuMCBdLCBbICJnZW4yIiwgMC4wIF0gXSwgImNvbXBsZXRlZFN0YWdlcyI6IFsgWyAiU1RBR0UgMSIsIFsgXSBdLCBbICJTVEFHRSAyIiwgWyBdIF0sIFsgIlNUQUdFIDEgKEhBUkQpIiwgWyBdIF0sIFsgIlNUQUdFIDMiLCBbIF0gXSBdLCAiQVRLIjogMC4wLCAic3RhbXBzIjogMC4wLCAidW5sb2NrZWRTdGFnZXMiOiBbICJTVEFHRSAxIiBdLCAidW5sb2NrZWRXZWFwb25zIjogWyAiUHN5Y2hvQXhlIiwgIkdsb3dzdGljayIsICJTcGlkZXJDb29raW5nIiwgIlRhaWxwbHVnIiwgIkJMQm9vayIsICJFbGl0ZUxhdmEiLCAiSG9sb0JvbWIiIF0sICJyZWdlbiI6IDAuMCwgInNwZWNDRFIiOiAwLjAsICJlbmhhbmNlVXAiOiAwLjAsICJFWFAiOiAwLjAsICJtb25leUdhaW4iOiAwLjAsICJyZXJvbGwiOiAwLjAsICJ3ZWFwb25MaW1pdCI6IDAuMCwgInRpbWVTdGFnZVNjb3JlcyI6IFsgWyAiVElNRSBTVEFHRSAxIiwgWyBdIF0gXSwgInNlZW5Db2xsYWJzIjogWyBdLCAiZW5jaGFudG1lbnRzIjogMC4wLCAiZmFuZG9tIjogMC4wLCAicmVmdW5kIjogMC4wLCAiY2hhbGxlbmdlIjogMC4wLCAidGltZU1vZGVVbmxvY2tlZCI6IDAuMCwgInVubG9ja2VkQ2hhcmFjdGVycyI6IDAuMCwgInVubG9ja2VkT3V0Zml0cyI6IFsgImRlZmF1bHQiIF0sICJlbGltaW5hdGUiOiAwLjAsICJyYW5kb21Nb25leUtleSI6IDIwNy4wLCAicGlja3VwUmFuZ2UiOiAwLjAsICJTUEQiOiAwLjAsICJEUiI6IDAuMCwgImNoYXJhY3RlcnMiOiBbIFsgImtyb25paSIsIDAuMCBdLCBbICJmdWJ1a2kiLCAwLjAgXSwgWyAiY2FsbGkiLCAxLjAgXSwgWyAibWVsIiwgMC4wIF0sIFsgInN1aXNlaSIsIDAuMCBdLCBbICJtYXRzdXJpIiwgMC4wIF0sIFsgImNob2NvIiwgMC4wIF0sIFsgImF5YW1lIiwgMC4wIF0sIFsgImhhYXRvIiwgMC4wIF0sIFsgInJhbmRvbSIsIDAuMCBdLCBbICJub25lIiwgMC4wIF0sIFsgInJvYm9jbyIsIDAuMCBdLCBbICJmYXVuYSIsIDAuMCBdLCBbICJzb3JhIiwgMC4wIF0sIFsgIm1pa28iLCAwLjAgXSwgWyAiZW1wdHkiLCAwLjAgXSwgWyAiZ3VyYSIsIDEuMCBdLCBbICJzYW5hIiwgMC4wIF0sIFsgIm9rYXl1IiwgMC4wIF0sIFsgImFraSIsIDAuMCBdLCBbICJpcnlzIiwgMC4wIF0sIFsgInNoaW9uIiwgMC4wIF0sIFsgImJhZSIsIDAuMCBdLCBbICJhemtpIiwgMC4wIF0sIFsgImtpYXJhIiwgMS4wIF0sIFsgImFxdWEiLCAwLjAgXSwgWyAiaW5hIiwgMS4wIF0sIFsgImtvcm9uZSIsIDAuMCBdLCBbICJtaW8iLCAwLjAgXSwgWyAiYW1lIiwgMS4wIF0sIFsgInN1YmFydSIsIDAuMCBdLCBbICJtdW1laSIsIDAuMCBdIF0sICJjaGFyYWN0ZXJDbGVhcnMiOiBbIF0sICJIUCI6IDAuMCwgImNyaXQiOiAwLjAgfQ==")

print(ans)
f = open("checker.txt", "w", encoding="latin-1")
f.write(ans)
f.close()