import base64
code="aW1wb3J0IHB5bW9uZ28KaW1wb3J0IHVybGxpYjIKaW1wb3J0IHVybGxpYgppbXBvcnQgY29va2llbGliCmltcG9ydCByYW5kb20KaW1wb3J0IHJlCmltcG9ydCBzdHJpbmcKaW1wb3J0IHN5cwppbXBvcnQgZ2V0b3B0CgojIGluaXQgdGhlIGdsb2JhbCBjb29raWUgamFyCmNqID0gY29va2llbGliLkNvb2tpZUphcigpCiMgZGVjbGFyZSB0aGUgdmFyaWFibGVzIHRvIGNvbm5lY3QgdG8gZGIKY29ubmVjdGlvbiA9IE5vbmUKZGIgPSBOb25lCndlYmhvc3QgPSAibG9jYWxob3N0OjgwODIiCm1vbmdvc3RyID0gIm1vbmdvZGI6Ly9sb2NhbGhvc3Q6MjcwMTciCmRiX25hbWUgPSAiYmxvZyIKCiMgdGhpcyBzY3JpcHQgd2lsbCBjaGVjayB0aGF0IGhvbWV3b3JrIDMuMiBpcyBjb3JyZWN0CgojIG1ha2VzIGEgbGl0dGxlIHNhbHQKZGVmIG1ha2Vfc2FsdChuKToKICAgIHNhbHQgPSAiIgogICAgZm9yIGkgaW4gcmFuZ2Uobik6CiAgICAgICAgc2FsdCA9IHNhbHQgKyByYW5kb20uY2hvaWNlKHN0cmluZy5hc2NpaV9sZXR0ZXJzKQogICAgcmV0dXJuIHNhbHQKCgojIHRoaXMgaXMgYSB2YWxpZGF0aW9uIHNjcmlwdCB0byBtYWtlIHN1cmUgdGhlIGJsb2cgd29ya3MgY29ycmVjdGx5LgoKZGVmIGNyZWF0ZV91c2VyKHVzZXJuYW1lLCBwYXNzd29yZCk6CiAgICAKICAgIGdsb2JhbCBjagoKICAgIHRyeToKICAgICAgICBwcmludCAiVHJ5aW5nIHRvIGNyZWF0ZSBhIHRlc3QgdXNlciAiLCB1c2VybmFtZQogICAgICAgIHVybCA9ICJodHRwOi8vezB9L3NpZ251cCIuZm9ybWF0KHdlYmhvc3QpCgogICAgICAgIGRhdGEgPSB1cmxsaWIudXJsZW5jb2RlKFsoImVtYWlsIiwiIiksKCJ1c2VybmFtZSIsdXNlcm5hbWUpLCAoInBhc3N3b3JkIixwYXNzd29yZCksICgidmVyaWZ5IixwYXNzd29yZCldKQogICAgICAgIHJlcXVlc3QgPSB1cmxsaWIyLlJlcXVlc3QodXJsPXVybCwgZGF0YT1kYXRhKQogICAgICAgIG9wZW5lciA9IHVybGxpYjIuYnVpbGRfb3BlbmVyKHVybGxpYjIuSFRUUENvb2tpZVByb2Nlc3NvcihjaikpCiAgICAgICAgZiA9IG9wZW5lci5vcGVuKHJlcXVlc3QpCgogICAgICAgIHVzZXJzID0gZGIudXNlcnMKICAgICAgICAjIGNoZWNrIHRoYXQgdGhlIHVzZXIgaXMgaW4gdXNlcnMgY29sbGVjdGlvbgogICAgICAgIHVzZXIgPSB1c2Vycy5maW5kX29uZSh7J19pZCc6dXNlcm5hbWV9KQogICAgICAgIGlmICh1c2VyID09IE5vbmUpOgogICAgICAgICAgICBwcmludCAiQ291bGQgbm90IGZpbmQgdGhlIHRlc3QgdXNlciAiLCB1c2VybmFtZSwgImluIHRoZSB1c2VycyBjb2xsZWN0aW9uLiIKICAgICAgICAgICAgcmV0dXJuIEZhbHNlCiAgICAgICAgcHJpbnQgIkZvdW5kIHRoZSB0ZXN0IHVzZXIgIiwgdXNlcm5hbWUsICIgaW4gdGhlIHVzZXJzIGNvbGxlY3Rpb24iCgogICAgICAgICMgY2hlY2sgdGhhdCB0aGUgdXNlciBoYXMgYmVlbiBidWlsdAogICAgICAgIHJlc3VsdCA9IGYucmVhZCgpCiAgICAgICAgZXhwciA9IHJlLmNvbXBpbGUoIldlbGNvbWVccysiKyB1c2VybmFtZSkKICAgICAgICBpZiBleHByLnNlYXJjaChyZXN1bHQpOgogICAgICAgICAgICByZXR1cm4gVHJ1ZQogICAgICAgIAogICAgICAgIHByaW50ICJXaGVuIHdlIHRyaWVkIHRvIGNyZWF0ZSBhIHVzZXIsIGhlcmUgaXMgdGhlIG91dHB1dCB3ZSBnb3RcbiIKICAgICAgICBwcmludCByZXN1bHQKICAgICAgICAKICAgICAgICByZXR1cm4gRmFsc2UKICAgIGV4Y2VwdDoKICAgICAgICBwcmludCAidGhlIHJlcXVlc3QgdG8gIiwgdXJsLCAiIGZhaWxlZCwgc28geW91ciBibG9nIG1heSBub3QgYmUgcnVubmluZy4iCiAgICAgICAgcmFpc2UKICAgICAgICByZXR1cm4gRmFsc2UKCgpkZWYgdHJ5X3RvX2xvZ2luKHVzZXJuYW1lLCBwYXNzd29yZCk6CgogICAgdHJ5OgogICAgICAgIHByaW50ICJUcnlpbmcgdG8gbG9naW4gZm9yIHRlc3QgdXNlciAiLCB1c2VybmFtZQogICAgICAgIHVybCA9ICJodHRwOi8vezB9L2xvZ2luIi5mb3JtYXQod2ViaG9zdCkKCiAgICAgICAgZGF0YSA9IHVybGxpYi51cmxlbmNvZGUoWygidXNlcm5hbWUiLHVzZXJuYW1lKSwgKCJwYXNzd29yZCIscGFzc3dvcmQpXSkKICAgICAgICByZXF1ZXN0ID0gdXJsbGliMi5SZXF1ZXN0KHVybD11cmwsIGRhdGE9ZGF0YSkKICAgICAgICBvcGVuZXIgPSB1cmxsaWIyLmJ1aWxkX29wZW5lcih1cmxsaWIyLkhUVFBDb29raWVQcm9jZXNzb3IoY2opKQogICAgICAgIGYgPSBvcGVuZXIub3BlbihyZXF1ZXN0KQoKICAgICAgICAjIGNoZWNrIGZvciBzdWNjZXNzZnVsIGxvZ2luCiAgICAgICAgcmVzdWx0ID0gZi5yZWFkKCkKICAgICAgICBleHByID0gcmUuY29tcGlsZSgiV2VsY29tZVxzKyIrIHVzZXJuYW1lKQogICAgICAgIGlmIGV4cHIuc2VhcmNoKHJlc3VsdCk6CiAgICAgICAgICAgIHJldHVybiBUcnVlCgogICAgICAgIHByaW50ICJXaGVuIHdlIHRyaWVkIHRvIGxvZ2luLCBoZXJlIGlzIHRoZSBvdXRwdXQgd2UgZ290XG4iCiAgICAgICAgcHJpbnQgcmVzdWx0CiAgICAgICAgcmV0dXJuIEZhbHNlCiAgICBleGNlcHQ6CiAgICAgICAgcHJpbnQgInRoZSByZXF1ZXN0IHRvICIsIHVybCwgIiBmYWlsZWQsIHNvIHlvdXIgYmxvZyBtYXkgbm90IGJlIHJ1bm5pbmcuIgogICAgICAgIHJldHVybiBGYWxzZQoKCmRlZiBhZGRfYmxvZ19wb3N0KHRpdGxlLHBvc3QsdGFncyk6CgogICAgdHJ5OgogICAgICAgIHByaW50ICJUcnlpbmcgdG8gc3VibWl0IGEgcG9zdCB3aXRoIHRpdGxlICIsIHRpdGxlCiAgICAgICAgZGF0YSA9IHVybGxpYi51cmxlbmNvZGUoWygiYm9keSIscG9zdCksICgic3ViamVjdCIsdGl0bGUpLCAoInRhZ3MiLHRhZ3MpXSkKICAgICAgICB1cmwgPSAiaHR0cDovL3swfS9uZXdwb3N0Ii5mb3JtYXQod2ViaG9zdCkKICAgICAgICByZXF1ZXN0ID0gdXJsbGliMi5SZXF1ZXN0KHVybD11cmwsIGRhdGE9ZGF0YSkKICAgICAgICBjai5hZGRfY29va2llX2hlYWRlcihyZXF1ZXN0KQogICAgICAgIG9wZW5lciA9IHVybGxpYjIuYnVpbGRfb3BlbmVyKCkKICAgICAgICBmID0gb3BlbmVyLm9wZW4ocmVxdWVzdCkKCiAgICAgICAgIyBjaGVjayBmb3Igc3VjY2Vzc2Z1bCBsb2dpbgogICAgICAgIHJlc3VsdCA9IGYucmVhZCgpCiAgICAgICAgZXhwciA9IHJlLmNvbXBpbGUodGl0bGUgKyAiLisiICsgcG9zdCwgcmUuRE9UQUxMKQoKICAgICAgICBpZiBleHByLnNlYXJjaChyZXN1bHQpOgogICAgICAgICAgICByZXR1cm4gVHJ1ZQoKICAgICAgICBwcmludCAiV2hlbiB3ZSB0cmllZCB0byBwb3N0LCBoZXJlIGlzIHRoZSBvdXRwdXQgd2UgZ290XG4iCiAgICAgICAgcHJpbnQgcmVzdWx0CiAgICAgICAgcmV0dXJuIEZhbHNlCgogICAgZXhjZXB0OgogICAgICAgIHByaW50ICJ0aGUgcmVxdWVzdCB0byAiLCB1cmwsICIgZmFpbGVkLCBzbyB5b3VyIGJsb2cgbWF5IG5vdCBiZSBydW5uaW5nLiIKICAgICAgICByYWlzZQoKICAgICAgICByZXR1cm4gRmFsc2UKCmRlZiBhZGRfYmxvZ19jb21tZW50KHRpdGxlLHBvc3QpOgoKICAgIHRyeToKICAgICAgICBwcmludCAiK1RyeWluZyB0byBzdWJtaXQgYSBibG9nIGNvbW1lbnQgZm9yIHBvc3Qgd2l0aCB0aXRsZSIsIHRpdGxlCiAgICAgICAgdXJsID0gImh0dHA6Ly97MH0vbmV3Y29tbWVudCIuZm9ybWF0KHdlYmhvc3QpCiAgICAgICAgCiAgICAgICAgZG9jID0ge30KICAgICAgICBjaGVja19tb25nb19mb3JfcG9zdCh0aXRsZSwgcG9zdCwgZG9jKQoKICAgICAgICBwZXJtYWxpbmsgPSBkb2NbJ2RvYyddWydwZXJtYWxpbmsnXQoKICAgICAgICBjb21tZW50X25hbWUgPSBtYWtlX3NhbHQoMTIpCiAgICAgICAgY29tbWVudF9ib2R5ID0gbWFrZV9zYWx0KDEyKQoKICAgICAgICBkYXRhID0gdXJsbGliLnVybGVuY29kZShbKCJjb21tZW50TmFtZSIsY29tbWVudF9uYW1lKSwgKCJjb21tZW50Qm9keSIsY29tbWVudF9ib2R5KSwgKCJwZXJtYWxpbmsiLHBlcm1hbGluayldKQogICAgICAgIHJlcXVlc3QgPSB1cmxsaWIyLlJlcXVlc3QodXJsPXVybCwgZGF0YT1kYXRhKQogICAgICAgIGNqLmFkZF9jb29raWVfaGVhZGVyKHJlcXVlc3QpCiAgICAgICAgb3BlbmVyID0gdXJsbGliMi5idWlsZF9vcGVuZXIoKQogICAgICAgIGYgPSBvcGVuZXIub3BlbihyZXF1ZXN0KQoKICAgICAgICAjIGNoZWNrIGZvciBzdWNjZXNzZnVsIGFkZGl0aW9uIG9mIGNvbW1lbnQgb24gcGFnZQogICAgICAgIHJlc3VsdCA9IGYucmVhZCgpCiAgICAgICAgZXhwciA9IHJlLmNvbXBpbGUodGl0bGUgKyAiLisiICsgcG9zdCwgcmUuRE9UQUxMKQoKICAgICAgICBpZiBub3QgZXhwci5zZWFyY2gocmVzdWx0KToKICAgICAgICAgICAgcHJpbnQgIldoZW4gd2UgdHJpZWQgdG8gZmluZCB0aGUgY29tbWVudCB3ZSBwb3N0ZWQgYXQgdGhlICAiLCB1cmwsICIgaGVyZSBpcyB3aGF0IHdlIGdvdCIKICAgICAgICAgICAgcHJpbnQgcmVzdWx0CiAgICAgICAgICAgIHJldHVybiBGYWxzZQoKCiAgICAgICAgIyBjaGVjayBmb3Igc3VjY2Vzc2Z1bCBhZGRpdGlvbiBvZiBjb21tZW50Li5yZXRyaWV2ZSB0aGUgZG9jIGFnYWluCiAgICAgICAgaWYobm90IGNoZWNrX21vbmdvX2Zvcl9wb3N0KHRpdGxlLCBwb3N0LCBkb2MpKToKICAgICAgICAgICAgcHJpbnQgIkNvdWxkIG5vdCBmaW5kIGNvbW1lbnQgaW4gZGF0YWJhc2UiCiAgICAgICAgICAgIHJldHVybiBGYWxzZQogICAgICAgIAogICAgICAgIGZvdW5kID0gRmFsc2UKICAgICAgICBpZiAoJ2NvbW1lbnRzJyBpbiBkb2NbJ2RvYyddKToKICAgICAgICAgICAgZm9yIGNvbW1lbnQgaW4gZG9jWydkb2MnXVsnY29tbWVudHMnXToKICAgICAgICAgICAgICAgIGlmIChjb21tZW50Wydib2R5J10gPT0gY29tbWVudF9ib2R5IGFuZCBjb21tZW50WydhdXRob3InXSA9PSBjb21tZW50X25hbWUpOgogICAgICAgICAgICAgICAgICAgIGZvdW5kID0gVHJ1ZQoKICAgICAgICByZXR1cm4gZm91bmQKCiAgICBleGNlcHQ6CiAgICAgICAgcHJpbnQgInRoZSByZXF1ZXN0IHRvICIsIHVybCwgIiBmYWlsZWQsIHNvIHlvdXIgYmxvZyBtYXkgbm90IGJlIHJ1bm5pbmcuIgogICAgICAgIHJhaXNlCgogICAgICAgIHJldHVybiBGYWxzZQoKCiMgZmV0Y2ggdGhlIGJsb2cgaG9tZSBwYWdlIGFuZCByZXR1cm4gdGhlIGxpbmsgb2YgdGhlIGZpcnN0IHBvc3QKZGVmIGZldGNoX2Jsb2dfaG9tZV9wYWdlKHBvc3RzKToKCiAgICB0cnk6CiAgICAgICAgdXJsID0gImh0dHA6Ly97MH0vIi5mb3JtYXQod2ViaG9zdCkKICAgICAgICBwcmludCAiVHJ5aW5nIHRvIGdyYWIgdGhlIGJsb2cgaG9tZSBwYWdlIGF0IHVybCBhbmQgZmluZCB0aGUgZmlyc3QgcG9zdC4iLCB1cmwKICAgICAgICByZXF1ZXN0ID0gdXJsbGliMi5SZXF1ZXN0KHVybD11cmwpCiAgICAgICAgY2ouYWRkX2Nvb2tpZV9oZWFkZXIocmVxdWVzdCkKICAgICAgICBvcGVuZXIgPSB1cmxsaWIyLmJ1aWxkX29wZW5lcigpCiAgICAgICAgZiA9IG9wZW5lci5vcGVuKHJlcXVlc3QpCgogICAgICAgICMgTG9vayBmb3IgYSBwb3N0CiAgICAgICAgcmVzdWx0ID0gZi5yZWFkKCkKICAgICAgICBleHByID0gcmUuY29tcGlsZSgiPGEgaHJlZj1cIihbXlwiXSspXCJcdyo/PiIsIHJlLkRPVEFMTCkKCgogICAgICAgIG1hdGNoID0gZXhwci5zZWFyY2gocmVzdWx0KQoKICAgICAgICBpZiBtYXRjaCBpcyBub3QgTm9uZToKICAgICAgICAgICAgcHJpbnQgIkZvdW5kIGEgcG9zdCB1cmw6ICIsIG1hdGNoLmdyb3VwKDEpCiAgICAgICAgICAgIHBvc3RzLmFwcGVuZChtYXRjaC5ncm91cCgxKSkKICAgICAgICAgICAgcmV0dXJuIFRydWUKCiAgICAgICAgCiAgICAgICAgcHJpbnQgIkhtbSwgY2FuJ3Qgc2VlbSB0byBmaW5kIGEgcG9zdC4gSXMgdGhlIGJsb2cgcG9wdWxhdGVkIHdpdGggcG9zdHM/IgogICAgICAgIHByaW50ICJXaGVuIHdlIHRyaWVkIHRvIHJlYWQgdGhlIGJsb2cgaW5kZXggYXQgIiwgdXJsLCAiIGhlcmUgaXMgd2hhdCB3ZSBnb3QiCiAgICAgICAgcHJpbnQgcmVzdWx0CiAgICAgICAgcmV0dXJuIEZhbHNlCgogICAgZXhjZXB0OgogICAgICAgIHByaW50ICJ0aGUgcmVxdWVzdCB0byAiLCB1cmwsICIgZmFpbGVkLCBzbyB5b3VyIGJsb2cgbWF5IG5vdCBiZSBydW5uaW5nLiIKICAgICAgICByYWlzZQoKICAgICAgICByZXR1cm4gRmFsc2UKCiMgZ2V0cyB0aGUgbGlrZXMgdmFsdWUgb2ZmIHRoZSBmaXJzdCBjb21tbWVudCBvciByZXR1cm5zIE5vbmUKZGVmIGZldGNoX2xpa2VzKHVybCk6CgogICAgdHJ5OgogICAgICAgIHVybCA9ICJodHRwOi8vezB9ezF9Ii5mb3JtYXQod2ViaG9zdCwgdXJsKQogICAgICAgIHByaW50ICJUcnlpbmcgdG8gZ3JhYiB0aGUgbnVtYmVyIG9mIGxpa2VzIGZvciB1cmwgIiwgdXJsCiAgICAgICAgcmVxdWVzdCA9IHVybGxpYjIuUmVxdWVzdCh1cmw9dXJsKQogICAgICAgIGNqLmFkZF9jb29raWVfaGVhZGVyKHJlcXVlc3QpCiAgICAgICAgb3BlbmVyID0gdXJsbGliMi5idWlsZF9vcGVuZXIoKQogICAgICAgIGYgPSBvcGVuZXIub3BlbihyZXF1ZXN0KQoKCiAgICAgICAgIyBsZXQncyBnZXQgdGhlIGZpcnN0IGZvcm0gZWxlbWVudAogICAgICAgIHJlc3VsdCA9IGYucmVhZCgpCiAgICAgICAgZXhwciA9IHJlLmNvbXBpbGUoIjxmb3JtW14+XSo+Lio/TGlrZXM6XHMqKFxkKylccyo8Lio/PC9mb3JtPiIsIHJlLkRPVEFMTCkKCiAgICAgICAgbWF0Y2ggPSBleHByLnNlYXJjaChyZXN1bHQpCgogICAgICAgIGlmIG1hdGNoIGlzIG5vdCBOb25lOgogICAgICAgICAgICBwcmludCAiTGlrZXMgdmFsdWUgIiwgbWF0Y2guZ3JvdXAoMSkKICAgICAgICAgICAgcmV0dXJuIGludChtYXRjaC5ncm91cCgxKSkKCiAgICAgICAgcHJpbnQgIkNhbid0IGZldGNoIHRoZSBsaWtlIHZhbHVlIGZvciB0aGUgZmlyc3QgY29tbWVudC4gUGVyaGFwcyB0aGUgYmxvZyBlbnRyeSBoYXMgbm8gY29tbWVudHM/IgogICAgICAgIHByaW50ICJXaGVuIHdlIHRyaWVkIHRvIHJlYWQgdGhlIGJsb2cgcGVybWFsaW5rIGF0ICIsIHVybCwgIiBoZXJlIGlzIHdoYXQgd2UgZ290IgogICAgICAgIHJldHVybiBOb25lCgogICAgZXhjZXB0OgogICAgICAgIHByaW50ICJ0aGUgcmVxdWVzdCB0byAiLCB1cmwsICIgZmFpbGVkLCBzbyB5b3VyIGJsb2cgbWF5IG5vdCBiZSBydW5uaW5nLiIKICAgICAgICByYWlzZQoKICAgICAgICByZXR1cm4gTm9uZQoKCiMgZ2V0cyB0aGUgbGlrZXMgdmFsdWUgb2ZmIHRoZSBmaXJzdCBjb21tbWVudCBvciByZXR1cm5zIE5vbmUKZGVmIGNsaWNrX29uX2xpa2UocGVybWFsaW5rKToKCiAgICBwcmludCAiQ2xpY2tpbmcgb24gTGlrZSBsaW5rIGZvciBwb3N0OiAiLCBwZXJtYWxpbmsKICAgIHRyeToKICAgICAgICBleHByID0gIHJlLmNvbXBpbGUoIlteL10rLyhbXi9dKykiKQogICAgICAgIG1hdGNoID0gZXhwci5zZWFyY2gocGVybWFsaW5rKQogICAgICAgIGlmIG1hdGNoIGlzIE5vbmU6CiAgICAgICAgICAgIHJldHVybiBGYWxzZQoKICAgICAgICBwZXJtYWxpbmsgPSBtYXRjaC5ncm91cCgxKQogICAgICAgIHVybCA9ICJodHRwOi8vezB9L2xpa2UiLmZvcm1hdCh3ZWJob3N0KQogICAgICAgICMgcHJpbnQgIkxpa2UgUE9TVCB1cmwiLCB1cmwKCiAgICAgICAgZGF0YSA9IHVybGxpYi51cmxlbmNvZGUoWygicGVybWFsaW5rIixwZXJtYWxpbmspLCAoImNvbW1lbnRfb3JkaW5hbCIsIjAiKV0pCiAgICAgICAgcmVxdWVzdCA9IHVybGxpYjIuUmVxdWVzdCh1cmw9dXJsLCBkYXRhPWRhdGEpCiAgICAgICAgY2ouYWRkX2Nvb2tpZV9oZWFkZXIocmVxdWVzdCkKICAgICAgICBvcGVuZXIgPSB1cmxsaWIyLmJ1aWxkX29wZW5lcigpCiAgICAgICAgZiA9IG9wZW5lci5vcGVuKHJlcXVlc3QpCgogICAgICAgIHJldHVybiBUcnVlCgogICAgZXhjZXB0OgogICAgICAgIHByaW50ICJ0aGUgcmVxdWVzdCB0byAiLCB1cmwsICIgZmFpbGVkLCBzbyB5b3VyIGJsb2cgbWF5IG5vdCBiZSBydW5uaW5nLiIKICAgICAgICByYWlzZQoKCgoKIyBjb21tYW5kIGxpbmUgYXJnIHBhcnNpbmcgdG8gbWFrZSBmb2xrcyBoYXBweSB3aG8gd2FudCB0byBydW4gYXQgbW9uZ29sYWJzIG9yIG1vbmdvaHEKIyB0aGlzIGZ1bmN0aW9ucyB1c2VzIGdsb2JhbCB2YXJzIHRvIGNvbW11bmljYXRlLiBmb3JnaXZlIG1lLgpkZWYgYXJnX3BhcnNpbmcoYXJndik6CgogICAgZ2xvYmFsIHdlYmhvc3QKICAgIGdsb2JhbCBtb25nb3N0cgogICAgZ2xvYmFsIGRiX25hbWUKCiAgICB0cnk6CiAgICAgICAgb3B0cywgYXJncyA9IGdldG9wdC5nZXRvcHQoYXJndiwgIi1wOi1tOi1kOiIpCiAgICBleGNlcHQgZ2V0b3B0LkdldG9wdEVycm9yOgogICAgICAgIHByaW50ICJ1c2FnZSB2YWxpZGF0ZS5weSAtcCB3ZWJob3N0IC1tIG1vbmdvQ29ubmVjdFN0cmluZyAtZCBkYXRhYmFzZU5hbWUiCiAgICAgICAgcHJpbnQgIlx0d2ViaG9zdCBkZWZhdWx0cyB0byB7MH0iLmZvcm1hdCh3ZWJob3N0KQogICAgICAgIHByaW50ICJcdG1vbmdvQ29ubmVjdGlvblN0cmluZyBkZWZhdWx0IHRvIHswfSIuZm9ybWF0KG1vbmdvc3RyKQogICAgICAgIHByaW50ICJcdGRhdGFiYXNlTmFtZSBkZWZhdWx0cyB0byB7MH0iLmZvcm1hdChkYl9uYW1lKQogICAgICAgIHN5cy5leGl0KDIpCiAgICBmb3Igb3B0LCBhcmcgaW4gb3B0czoKICAgICAgICBpZiAob3B0ID09ICctaCcpOgogICAgICAgICAgICBwcmludCAidXNhZ2UgdmFsaWRhdGUucHkgLXAgd2ViaG9zdCAtbSBtb25nb0Nvbm5lY3RTdHJpbmcgLWQgZGF0YWJhc2VOYW1lIgogICAgICAgICAgICBzeXMuZXhpdCgyKQogICAgICAgIGVsaWYgb3B0IGluICgiLXAiKToKICAgICAgICAgICAgd2ViaG9zdCA9IGFyZwogICAgICAgICAgICBwcmludCAiT3ZlcnJpZGluZyBIVFRQIGhvc3QgdG8gYmUgIiwgd2ViaG9zdAogICAgICAgIGVsaWYgb3B0IGluICgiLW0iKToKICAgICAgICAgICAgbW9uZ29zdHIgPSBhcmcKICAgICAgICAgICAgcHJpbnQgIk92ZXJyaWRpbmcgTW9uZ29EQiBjb25uZWN0aW9uIHN0cmluZyB0byBiZSAiLCBtb25nb3N0cgogICAgICAgIGVsaWYgb3B0IGluICgiLWQiKToKICAgICAgICAgICAgZGJfbmFtZSA9IGFyZwogICAgICAgICAgICBwcmludCAiT3ZlcnJpZGluZyBNb25nb0RCIGRhdGFiYXNlIHRvIGJlICIsIGRiX25hbWUKICAgICAgICAgICAgCgoKIyBtYWluIHNlY3Rpb24gb2YgdGhlIGNvZGUKZGVmIG1haW4oYXJndik6CiAgICAgICAgICAgIAogICAgYXJnX3BhcnNpbmcoYXJndikKICAgIGdsb2JhbCBjb25uZWN0aW9uCiAgICBnbG9iYWwgZGIKCiAgICBwcmludCAiV2VsY29tZSB0byB0aGUgTTEwMSBGaW5hbCBFeGFtLCBRdWVzdGlvbiA0IFZhbGlkYXRpb24gQ2hlY2tlciIKCiAgICAjIGNvbm5lY3QgdG8gdGhlIGRiIChtb25nb3N0ciB3YXMgc2V0IGluIGFyZ19wYXJzaW5nKQogICAgY29ubmVjdGlvbiA9IHB5bW9uZ28uTW9uZ29DbGllbnQobW9uZ29zdHIpCiAgICBkYiA9IGNvbm5lY3Rpb25bZGJfbmFtZV0KCgogICAgIyBncmFiIHRoZSBibG9nIGhvbWUgcGFnZSBhbmQgZmluZCB0aGUgZmlyc3QgcG9zdAogICAgcG9zdHMgPSBbXQogICAgaWYgKG5vdCBmZXRjaF9ibG9nX2hvbWVfcGFnZShwb3N0cykpOgogICAgICAgIHByaW50ICJJIGNhbid0IGdyYWIgdGhlIGhvbWUgcGFnZSBvZiB0aGUgYmxvZyIKICAgICAgICBzeXMuZXhpdCgxKQoKICAgICMgbm93IGdvIHRvIHRoZSBwZXJtYWxpbmsgcGFnZSBmb3IgdGhhdCBwb3N0CiAgICBsaWtlc192YWx1ZSA9IGZldGNoX2xpa2VzKHBvc3RzWzBdKQoKICAgIGlmIChsaWtlc192YWx1ZSBpcyAgTm9uZSk6CiAgICAgICAgcHJpbnQgIkNhbid0IGZldGNoIHRoZSBsaWtlIHZhbHVlIgogICAgICAgIHN5cy5leGl0KDEpCgogICAgY2xpY2tfb25fbGlrZShwb3N0c1swXSkKCiAgICBuZXdfbGlrZXNfdmFsdWUgPSBmZXRjaF9saWtlcyhwb3N0c1swXSkKCiAgICBpZiAobmV3X2xpa2VzX3ZhbHVlICE9IChsaWtlc192YWx1ZSArIDEpKToKICAgICAgICBwcmludCAiSSB3YXMgbm90IGFibGUgdG8gaW5jcmVtZW50IHRoZSBsaWtlcyBvbiBhIGNvbW1lbnQiCiAgICAgICAgcHJpbnQgIm9sZCBsaWtlcyB2YWx1ZSB3YXMgIiwgbGlrZXNfdmFsdWUKICAgICAgICBwcmludCAibGlrZXMgdmFsdWUgYWZ0ZXIgSSBjbGlja2VkIHdhcyAiLCBuZXdfbGlrZXNfdmFsdWUKICAgICAgICBwcmludCAiU29ycnksIHlvdSBoYXZlIG5vdCBzb2x2ZWQgaXQgeWV0LiIKICAgICAgICBzeXMuZXhpdCgxKQoKCiAgICBwcmludCAiVGVzdHMgUGFzc2VkIGZvciBGaW5hbCA0LiBZb3VyIHZhbGlkYXRpb24gY29kZSBpcyAzZjgzN2hoZzY3M2doZDkzaGdmOCIKCgppZiBfX25hbWVfXyA9PSAiX19tYWluX18iOgogICAgbWFpbihzeXMuYXJndlsxOl0pCg=="

# Compatible for Python 3.6
with open('validate_q4.py', 'x') as f:
    f.write(base64.b64decode(code).decode())

# eval(compile(base64.b64decode(code), "<string>", 'exec'))
