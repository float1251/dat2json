# -*- coding: utf-8 -*-
import unittest
from expectpy import expect
from dat2json import dat2dic, dat2json


class Dat2JsonTest(unittest.TestCase):

    def setUp(self):
        with open("fixtures/sample.dat") as f:
            self.dat = f.read()

    def tearDown(self):
        pass

    def test_define_function(self):
        expect(dat2json).to_not.be_None

    def test_parse_first_line(self):
        expect(self.dat).to_not.be_None
        ret = dat2dic(self.dat)
        json = ret[0]
        expect(json).to_not.be_None
        expect(json["name"]).to.eql("名前")
        expect(json["mail"]).to.eql("メール欄")
        expect(json["comment"]).to.eql(" 本文 ")
        expect(json["datatime"]).to.eql("年/月/日（曜） 時:分:秒.下二桁（無い板もある）")
        expect(json["id"]).to.eql("hogehoge0")
        expect(json["title"]).to.eql("スレタイ")

        json = ret[1]
        expect(json).to_not.be_None
        expect(json["name"]).to.eql("名前")
        expect(json["mail"]).to.eql("メール欄")
        expect(json["comment"]).to.eql(" 本文 ")
        expect(json["datatime"]).to.eql("年/月/日（曜） 時:分:秒.下二桁（無い板もある）")
        expect(json["id"]).to.eql("hogehoge0")
        expect(json).to_not.have.ownProperty("title")

if __name__ == "__main__":
    unittest.main()
