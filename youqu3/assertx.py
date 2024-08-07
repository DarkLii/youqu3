#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
# SPDX-FileCopyrightText: 2023 UnionTech Software Technology Co., Ltd.
# SPDX-License-Identifier: GPL-2.0-only
import os
from typing import Union

from youqu3 import exceptions
from youqu3 import log, logger, setting
from youqu3.cmd import Cmd


@log
class Assert:
    """
    自定义断言类
    """

    @staticmethod
    def assert_image_exist(
            widget: str,
            rate: float = None,
            multiple: bool = False,
            picture_abspath: str = None,
            network_retry: int = None,
            pause: [int, float] = None,
            timeout: [int, float] = None,
            match_number: int = None,
    ):
        """
        期望界面存在模板图片
        :param widget: 图片路径 例：assert_res/1.png
        :param rate: 匹配相似度
        """
        logger.info(f"屏幕上匹配图片< {f'***{widget[-40:]}' if len(widget) >= 40 else widget} >")
        from youqu3.gui import pylinuxauto
        try:
            pylinuxauto.find_element_by_image(
                widget,
                rate=rate,
                multiple=multiple,
                picture_abspath=picture_abspath,
                network_retry=network_retry,
                pause=pause,
                timeout=timeout,
                max_match_number=match_number,
            )
        except exceptions.TemplateElementNotFound as exc:
            raise AssertionError(exc) from exceptions.TemplateElementNotFound

    @classmethod
    def assert_image_exist_during_time(
            cls,
            widget: str,
            screen_time: Union[float, int],
            rate: float = None,
            pause: Union[int, float] = None,
    ):
        """
        在一段时间内截图多张图片进行识别，其中有一张图片识别成功即返回结果;
        适用于气泡类的断言，比如气泡在1秒内消失，如果用常规的图像识别则有可能无法识别到；
        :param image_path: 要识别的模板图片；
        :param screen_time: 截取屏幕图片的时间，单位秒；
        :param rate: 识别率；
        :param pause: 截取屏幕图片的间隔时间，默认不间隔；
        """
        logger.info(f"屏幕上匹配图片< {f'***{widget[-40:]}' if len(widget) >= 40 else widget} >")
        from youqu3.gui import pylinuxauto
        try:
            pylinuxauto.get_during(widget, screen_time, rate, pause)
        except exceptions.TemplateElementNotFound as exc:
            raise AssertionError(exc) from exceptions.TemplateElementNotFound

    @staticmethod
    def assert_image_not_exist(
            widget: str,
            rate: float = None,
            multiple: bool = False,
            picture_abspath: str = None,
            network_retry: int = None,
            pause: [int, float] = None,
            timeout: [int, float] = None,
            match_number: int = None,
    ):
        """
        期望界面不存在模板图片
        :param widget: 图片路径 assert_res/1.png
        :param rate: 匹配相似度
        """
        logger.info(
            f"屏幕上匹配不存在图片< {f'***{widget[-40:]}' if len(widget) >= 40 else widget} >"
        )
        try:
            from youqu3.gui import pylinuxauto
            pylinuxauto.find_element_by_image(
                widget,
                rate=rate,
                multiple=multiple,
                picture_abspath=picture_abspath,
                network_retry=network_retry,
                pause=pause,
                timeout=timeout,
                max_match_number=match_number,
            )
            raise exceptions.TemplateElementFound(widget)
        except exceptions.TemplateElementNotFound:
            pass
        except exceptions.TemplateElementFound as exc:
            raise AssertionError(exc) from exceptions.TemplateElementFound

    @staticmethod
    def assert_file_exist(file_path):
        """
        期望存在文件路径
        :param file_path: 文件全路径或目录 例：~/Desktop/1.txt
        """
        logger.info(f"断言文件存在 <{file_path}>")
        if not os.path.exists(os.path.expanduser(file_path)):
            raise AssertionError(f"文件不存在:{file_path}")
        return True

    @staticmethod
    def assert_file_not_exist(file_path):
        """
        期望不存在文件路径
        :param file_path: 文件全路径 例：~/Desktop/1.txt
        :param file: 文件名
        :param recursive: 是否递归查找
        """
        logger.info(f"断言文件不存在 <{file_path}>")
        if os.path.exists(os.path.expanduser(file_path)):
            raise AssertionError(f"文件存在:{file_path}")

    @staticmethod
    def assert_element_exist(expr):
        """
         期望元素存在
        :param expr: 匹配元素的格式, 例如： /dde-file-manager/1.txt
        """
        logger.info(f"断言元素存在<{expr}>")
        from youqu3.gui import pylinuxauto
        if not pylinuxauto.find_element_by_attr_path(expr):
            raise AssertionError(f"元素不存在:{expr}")

    @staticmethod
    def assert_element_not_exist(expr):
        """
         期望元素不存在
        :param expr: 匹配元素的格式
        """
        logger.info(f"断言元素不存在<{expr}>")
        from youqu3.gui import pylinuxauto
        try:
            pylinuxauto.find_element_by_attr_path(expr)
            raise AssertionError(f"元素不应该存在:{expr}")
        except exceptions.ElementNotFound:
            pass

    @staticmethod
    def assert_process_exist(app):
        """
         断言应用进程存在
        :param app: 应用名字
        """
        logger.info(f"断言应用进程状态{app}存在")
        if True != Cmd.get_process_status(app):
            raise AssertionError(f"断言应用进程状态{app}不存在")

    @staticmethod
    def assert_process_not_exist(app):
        """
         断言应用进程不存在
        :param app: 应用名字
        """
        logger.info(f"断言应用进程状态{app}不存在")
        if False != Cmd.get_process_status(app):
            raise AssertionError(f"断言应用进程状态{app}存在")

    @staticmethod
    def assert_equal(expect, actual):
        """
         断言相等
        :param expect: 期望结果
        :param actual: 实际结果
        """
        logger.info(f"预期值<{expect}>与实际值<{actual}>是否相等")
        if not bool(expect == actual):
            raise AssertionError(f"预期值<{expect}>与实际值<{actual}>不相等")

    @staticmethod
    def assert_not_equal(expect, actual):
        """
         断言不相等
        :param expect: 期望结果
        :param actual: 实际结果
        """
        logger.info(f"预期值<{expect}>与实际值<{actual}>是否相等")
        if bool(expect == actual):
            raise AssertionError(f"预期值<{expect}>与实际值<{actual}>不相等")

    @staticmethod
    def assert_true(expect):
        """
         断言结果为真
        :param expect: 结果
        """
        if not expect:
            raise AssertionError(f"<{expect}>不为真")

    @staticmethod
    def assert_false(expect):
        """
         断言结果为假
        :param expect: 结果
        """
        if expect:
            raise AssertionError(f"<{expect}>不为假")

    @staticmethod
    def assert_ocr_exist(
            *args,
            picture_abspath=None,
            similarity=0.6,
            return_first=False,
            lang="ch",
            network_retry: int = None,
            pause: [int, float] = None,
            timeout: [int, float] = None,
            max_match_number: int = None,
            mode: str = "all",
    ):
        """
        断言文案存在
        :param args:
            目标字符,识别一个字符串或多个字符串,并返回其在图片中的坐标;
            如果不传参，返回图片中识别到的所有字符串。
        :param picture_abspath: 要识别的图片路径，如果不传默认截取全屏识别。
        :param similarity: 匹配度。
        :param return_first: 只返回第一个,默认为 False,返回识别到的所有数据。
        :param lang: `ch`, `en`, `fr`, `german`, `korean`, `japan`
        :param network_retry: 连接服务器重试次数
        :param pause: 重试间隔时间,单位秒
        :param timeout: 最大匹配超时,单位秒
        :param max_match_number: 最大匹配次数
        :param mode: "all" or "any"，all 表示识别所有目标字符，any 表示识别任意一个目标字符，默认值为 all
        """
        pic = None
        if picture_abspath is not None:
            pic = picture_abspath + ".png"

        from youqu3.gui import pylinuxauto

        res = pylinuxauto.find_element_by_ocr(
            *args,
            picture_abspath=pic,
            similarity=similarity,
            return_first=return_first,
            lang=lang,
            network_retry=network_retry,
            pause=pause,
            timeout=timeout,
            max_match_number=max_match_number,
        )
        if res is False:
            raise AssertionError(
                (f"通过OCR未识别到：{args}", f"{pic if pic else setting.SCREEN_CACHE}")
            )
        if isinstance(res, tuple):
            pass
        elif isinstance(res, dict):
            mode = mode.lower()
            if mode == "all" and False in res.values():
                res = filter(lambda x: x[1] is False, res.items())
                raise AssertionError(
                    (
                        f"通过OCR未识别到：{dict(res)}",
                        f"{pic if pic else setting.SCREEN_CACHE}",
                    )
                )
            elif mode == "any" and len(res) == list(res.values()).count(False):
                raise AssertionError(
                    (
                        f"通过OCR未识别到：{args}中的任意一个",
                        f"{pic if pic else setting.SCREEN_CACHE}",
                    )
                )

    @staticmethod
    def assert_ocr_not_exist(
            *args,
            picture_abspath=None,
            similarity=0.6,
            return_first=False,
            lang="ch",
            network_retry: int = None,
            pause: [int, float] = None,
            timeout: [int, float] = None,
            max_match_number: int = None,
    ):
        """断言文案不存在"""
        pic = None
        if picture_abspath is not None:
            pic = picture_abspath + ".png"
        from youqu3.gui import pylinuxauto

        res = pylinuxauto.find_element_by_ocr(
            *args,
            picture_abspath=pic,
            similarity=similarity,
            return_first=return_first,
            lang=lang,
            network_retry=network_retry,
            pause=pause,
            timeout=timeout,
            max_match_number=max_match_number,
        )
        if res is False:
            pass
        elif isinstance(res, tuple):
            raise AssertionError(
                (
                    f"通过ocr识别到不应存在的文案 {res}",
                    f"{pic if pic else setting.SCREEN_CACHE}",
                )
            )
        elif isinstance(res, dict) and True in res.values():
            res = filter(lambda x: x[1] is not False, res.items())
            raise AssertionError(
                (
                    f"通过OCR识别到不应存在的文案：{dict(res)}",
                    f"{pic if pic else setting.SCREEN_CACHE}",
                )
            )
