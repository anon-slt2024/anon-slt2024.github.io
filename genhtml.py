#!/usr/bin/env python3

from jinja2 import FileSystemLoader, Environment

import os
from glob import glob

def gen_rows(gtype, lang):

    ret = []
    if lang=="vi":

        freevc = './data/Vietnamese/freevc'
        freevc_sr = './data/Vietnamese/freevc_sr'
        freevc_kt_wo_asr = './data/Vietnamese/freevc_kt_wo_asr'
        freevc_kt = './data/Vietnamese/freevc_kt'
        freevc_kt_sr = './data/Vietnamese/freevc_kt_sr'
        freevc_kt_sr_200_10 = './data/Vietnamese/freevc_kt_sr_200_10'
        freevc_kt_sr_500_25 = './data/Vietnamese/freevc_kt_sr_500_25'
        f = open("data/demo_vi.txt", "r", encoding="utf8").readlines()
        for line in f:
            line = line.strip()
            [src_basename, tgt_basename, out] = line.split("|")
            if gtype in line and gtype=="s2s":
                src = os.path.join('data/seen_vi', src_basename)
                tgt = os.path.join('data/seen_vi', tgt_basename)
                row = (
                    src_basename,
                    tgt_basename,
                    src, 
                    tgt,
                    os.path.join(freevc, out),
                    os.path.join(freevc_sr, out),
                    os.path.join(freevc_kt_wo_asr, out),
                    os.path.join(freevc_kt, out),
                    os.path.join(freevc_kt_sr, out),
                    os.path.join(freevc_kt_sr_500_25, out),
                    os.path.join(freevc_kt_sr_200_10, out),
                )
                ret.append(row)
            elif gtype in line and gtype=="u2s":
                src = os.path.join('data/unseen_vi', src_basename)
                tgt = os.path.join('data/seen_vi', tgt_basename)
                row = (
                    src_basename,
                    tgt_basename,
                    src, 
                    tgt,
                    os.path.join(freevc, out),
                    os.path.join(freevc_sr, out),
                    os.path.join(freevc_kt_wo_asr, out),
                    os.path.join(freevc_kt, out),
                    os.path.join(freevc_kt_sr, out),
                    os.path.join(freevc_kt_sr_500_25, out),
                    os.path.join(freevc_kt_sr_200_10, out),
                )
                ret.append(row)
            elif gtype in line and gtype=="s2u":
                src = os.path.join('data/seen_vi', src_basename)
                tgt = os.path.join('data/unseen_vi', tgt_basename)
                row = (
                    src_basename,
                    tgt_basename,
                    src, 
                    tgt,
                    os.path.join(freevc, out),
                    os.path.join(freevc_sr, out),
                    os.path.join(freevc_kt_wo_asr, out),
                    os.path.join(freevc_kt, out),
                    os.path.join(freevc_kt_sr, out),
                    os.path.join(freevc_kt_sr_500_25, out),
                    os.path.join(freevc_kt_sr_200_10, out),
                )
                ret.append(row)
            elif gtype in line and gtype=="u2u":
                src = os.path.join('data/unseen_vi', src_basename)
                tgt = os.path.join('data/unseen_vi', tgt_basename)
                row = (
                    src_basename,
                    tgt_basename,
                    src, 
                    tgt,
                    os.path.join(freevc, out),
                    os.path.join(freevc_sr, out),
                    os.path.join(freevc_kt_wo_asr, out),
                    os.path.join(freevc_kt, out),
                    os.path.join(freevc_kt_sr, out),
                    os.path.join(freevc_kt_sr_500_25, out),
                    os.path.join(freevc_kt_sr_200_10, out),
                )

                ret.append(row)
            
        return ret


    if lang=="en":

        freevc = './data/English/freevc'
        freevc_sr = './data/English/freevc_sr'
        freevc_kt_wo_asr = './data/English/freevc_kt_wo_asr'
        freevc_kt = './data/English/freevc_kt'
        freevc_kt_sr = './data/English/freevc_kt_sr'
        freevc_kt_sr_200_10 = './data/English/freevc_kt_sr_200_10'
        freevc_kt_sr_500_25 = './data/English/freevc_kt_sr_500_25'
        f = open("data/demo_en.txt", "r", encoding="utf8").readlines()
        for line in f:
            line = line.strip()
            [src_basename, tgt_basename, out] = line.split("|")
            if gtype in line and gtype=="s2s":
                src = os.path.join('data/seen_en', src_basename)
                tgt = os.path.join('data/seen_en', tgt_basename)
                row = (
                    src_basename,
                    tgt_basename,
                    src, 
                    tgt,
                    os.path.join(freevc, out),
                    os.path.join(freevc_sr, out),
                    os.path.join(freevc_kt_wo_asr, out),
                    os.path.join(freevc_kt, out),
                    os.path.join(freevc_kt_sr, out),
                    os.path.join(freevc_kt_sr_500_25, out),
                    os.path.join(freevc_kt_sr_200_10, out),
                )
                ret.append(row)
            elif gtype in line and gtype=="u2s":
                src = os.path.join('data/unseen_en', src_basename)
                tgt = os.path.join('data/seen_en', tgt_basename)
                row = (
                    src_basename,
                    tgt_basename,
                    src, 
                    tgt,
                    os.path.join(freevc, out),
                    os.path.join(freevc_sr, out),
                    os.path.join(freevc_kt_wo_asr, out),
                    os.path.join(freevc_kt, out),
                    os.path.join(freevc_kt_sr, out),
                    os.path.join(freevc_kt_sr_500_25, out),
                    os.path.join(freevc_kt_sr_200_10, out),
                )
                ret.append(row)
            elif gtype in line and gtype=="s2u":
                src = os.path.join('data/seen_en', src_basename)
                tgt = os.path.join('data/unseen_en', tgt_basename)
                row = (
                    src_basename,
                    tgt_basename,
                    src, 
                    tgt,
                    os.path.join(freevc, out),
                    os.path.join(freevc_sr, out),
                    os.path.join(freevc_kt_wo_asr, out),
                    os.path.join(freevc_kt, out),
                    os.path.join(freevc_kt_sr, out),
                    os.path.join(freevc_kt_sr_500_25, out),
                    os.path.join(freevc_kt_sr_200_10, out),
                )
                ret.append(row)
            elif gtype in line and gtype=="u2u":
                src = os.path.join('data/unseen_en', src_basename)
                tgt = os.path.join('data/unseen_en', tgt_basename)
                row = (
                    src_basename,
                    tgt_basename,
                    src, 
                    tgt,
                    os.path.join(freevc, out),
                    os.path.join(freevc_sr, out),
                    os.path.join(freevc_kt_wo_asr, out),
                    os.path.join(freevc_kt, out),
                    os.path.join(freevc_kt_sr, out),
                    os.path.join(freevc_kt_sr_500_25, out),
                    os.path.join(freevc_kt_sr_200_10, out),
                )

                ret.append(row)
            
        return ret

def main():
    """Main function."""
    loader = FileSystemLoader(searchpath="./templates")
    env = Environment(loader=loader)
    template = env.get_template("base.html.jinja2")

    vi_s2s_rows = gen_rows("s2s", "vi")
    vi_s2u_rows = gen_rows("s2u", "vi")
    vi_u2s_rows = gen_rows("u2s", "vi")
    vi_u2u_rows = gen_rows("u2u", "vi")

    en_s2s_rows = gen_rows("s2s", "en")
    en_s2u_rows = gen_rows("s2u", "en")
    en_u2s_rows = gen_rows("u2s", "en")
    en_u2u_rows = gen_rows("u2u", "en")

    html = template.render(
        vi_s2s_rows=vi_s2s_rows,
        vi_s2u_rows=vi_s2u_rows,
        vi_u2s_rows=vi_u2s_rows,
        vi_u2u_rows=vi_u2u_rows,
        en_s2s_rows=en_s2s_rows,
        en_s2u_rows=en_s2u_rows,
        en_u2s_rows=en_u2s_rows,
        en_u2u_rows=en_u2u_rows,
    )
    # print(s2s_rows)
    # print(html)
    f = open("index.html", "w", encoding="utf8")
    f.write(html)

if __name__ == "__main__":
    main()
