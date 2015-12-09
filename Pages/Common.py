from time import sleep
from hotdog.FindEither import FindEither

__author__ = 'brian.menzies'
from webium import Find, Finds
from appium.webdriver.common.mobileby import MobileBy as By
from Helpers.BasePage import CBCWebBase
from selenium.webdriver.remote.webelement import WebElement
from time import sleep

class Footer(WebElement):
    linkTermsOfUse = Find(by=By.LINK_TEXT, value='Terms of Use')
    linkPrivacyPolicy = Find(by=By.LINK_TEXT, value='Privacy Policy')
    linkReusePermission = Find(by=By.LINK_TEXT, value='Reuse & Permission')
    linkHelp = Find(by=By.LINK_TEXT, value='Help')
    imgFooterLogo = Find(by=By.CSS_SELECTOR, value='.client-logo-footer')
    txtCopywrite = Find(by=By.CSS_SELECTOR, value='.footer-client-attr > p')

class NavBar(WebElement):
    btnToggle = Find(by=By.CLASS_NAME, value='toggle')
    btnShows = Find(by=By.LINK_TEXT, value='SHOWS')
    btnFeatured = Find(by=By.LINK_TEXT, value='FEATURED')
    btnDocumentaries = Find(by=By.LINK_TEXT, value='DOCUMENTARIES')
    btnKids = Find(by=By.LINK_TEXT, value='KIDS')


class CommonPage(CBCWebBase):
    navbar = FindEither(ui_type=NavBar, selectors= [[By.CLASS_NAME, 'nav-bar'],
                                                    [By.CLASS_NAME, 'nav-menu']])
    footer = Find(Footer, by=By.CLASS_NAME, value='footer-section')
    btnHome = Find(by=By.CLASS_NAME, value='client-logo-nav')
    genreDropdown = Find(by=By.CLASS_NAME, value='controls-label')
    loadingContainer = Find(by=By.CLASS_NAME, value='loading-container')
    loadingIndicator = Find(by=By.CLASS_NAME, value='loading-indicator loading')
    loadingContent = Find(by=By.CLASS_NAME, value='loading')
    carousel = Find(by=By.CLASS_NAME, value='carousel')
    carouselDots = Find(by=By.CLASS_NAME, value='carousel-dots')

    btnActiveCarouselDot = Find(by=By.CLASS_NAME, value='carousel-dot-active')
    btnCarouselDots = Finds(by=By.CLASS_NAME, value='carousel-dot')
    btnPlayPauseCarousel = Find(by=By.CLASS_NAME, value='carousel-play-pause')
    txtCarouselTagline = Find(by=By.CLASS_NAME, value='tagline-title')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def navigateToSection(self, SectionName):
        try:
            if self.elemenent_exists(self.navbar.btnToggle):
                if 'open' not in self.navbar.btnToggle.get_attribute('class'):
                    self.navbar.btnToggle.click()
                    sleep(1)
        except:
            pass
        section = SectionName.lower()
        if section.lower() == 'home':
            self.navbar.btnHome.click()
        elif section.lower() == 'featured':
            self.navbar.btnFeatured.click()
        elif section.lower() == 'shows':
            self.navbar.btnShows.click()
        elif section.lower() == 'documentaries':
            self.navbar.btnDocumentaries.click()
        elif section.lower() == 'kids':
            self.navbar.btnKids.click()
        else:
            pass

    def clickFeaturedItem(self, listOfItems, numberOfItem):
        print(listOfItems)
        number = int(numberOfItem) - 1
        listOfItems[number].click()

    def assertDropdownIsPresent(self):
        dropdownText = self.genreDropdown.text
        loweredText = dropdownText.lower()
        assert loweredText == 'genre', 'The Genre Dropdown Could Not Be Found'

    def getCurrentCarouselTitle(self):
        tagline = self.txtCarouselTagline.text
        return tagline

    def pauseCarousel(self):
        self.btnPlayPauseCarousel.click()
        sleep(1)

    def testCarousel(self):
        carouselInfo = str(self.btnActiveCarouselDot.text)
        splitNumbers = carouselInfo.split()
        firstArrayNumber = splitNumbers[1]
        finalArrayNumber = splitNumbers[3]
        firstNumber = int(firstArrayNumber)
        finalNumber = int(finalArrayNumber) - 1

        number = firstNumber
        for item in range(finalNumber):
            currentCarouselTitle = self.getCurrentCarouselTitle()
            self.btnCarouselDots[number].click()
            #Put a pause between switches or else chrome tests will fail
            sleep(2)
            newCarouselTitle = self.getCurrentCarouselTitle()
            assert currentCarouselTitle != newCarouselTitle, 'Expected Different Values. Instead (%s) and (%s) were found' % (currentCarouselTitle, newCarouselTitle)
            number += 1

        number = finalNumber - 1
        for items in range(finalNumber):
            currentCarouselTitle = self.getCurrentCarouselTitle()
            self.btnCarouselDots[number].click()
            #Put a pause between switches or else chrome tests will fail
            sleep(2)
            newCarouselTitle = self.getCurrentCarouselTitle()
            assert currentCarouselTitle != newCarouselTitle, 'Expected Different Values. Instead (%s) and (%s) were found' % (currentCarouselTitle, newCarouselTitle)
            number -= 1

