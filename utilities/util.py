"""
@package utilities

Util class implementation

"""
import time
import traceback
import random
import utilities.custom_logger as cl
import logging


class Util(object):
    log = cl.custom_logger(logging.INFO)

    @staticmethod
    def generate_email():
        lst = ['.']
        basic_email = 'pawelautomatyzacja'
        basic_email = (''.join("{}{}".format(x, random.choice(lst) if random.randint(0, 1) else '')
                               for x in basic_email)) + 'a@gmail.com'
        return basic_email

    def sleep(self, sec, info=''):
        """
        Put the program to wait for the specified amount of time
        """
        if info is not None:
            self.log.info("Wait :: '" + str(sec) + "' seconds for " + info)
        try:
            time.sleep(sec)
        except InterruptedError:
            traceback.print_stack()

    def verify_text_contains(self, actual_text, expected_text):
        """
        Verify actual text contains expected text string

        Parameters:
            expectedList: Expected Text
            actualList: Actual Text
        """
        self.log.info("Actual Text From Application Web UI --> :: " + actual_text)
        self.log.info("Expected Text From Application Web UI --> :: " + expected_text)
        if expected_text.lower() in actual_text.lower():
            self.log.info("### VERIFICATION CONTAINS !!!")
            return True
        else:
            self.log.info("### VERIFICATION DOES NOT CONTAINS !!!")
            return False
