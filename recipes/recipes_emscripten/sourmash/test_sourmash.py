def test_simple_save_load(selenium):
    from pathlib import Path
    from tempfile import TemporaryDirectory

    import sourmash

    mh = sourmash.MinHash(0, 5, scaled=1)
    mh.add_sequence("ACGTAGGTATAGGATACCTCGCTAGTACGTGCA")
    ss = sourmash.SourmashSignature(mh, name="foo")

    with TemporaryDirectory() as td:
        name = Path(td) / "test.sig"
        with open(name, "w") as fp:
            sourmash.save_signatures([ss], fp=fp)

        loaded = sourmash.load_one_signature(str(name))
        assert loaded == ss
