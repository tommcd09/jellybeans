# jellybeans

## About The Project

### Introduction

This project examines a phenomenon known as the "wisdom of crowds." It analyzes 126 responses to a [survey](https://forms.gle/nJrzYPWguhfQbg8x5) asking Reddit and Facebook users to guess how many jelly beans are in a pictured glass vase.

This project attempts to answer the following questions:

1. How well does the mean or median of a crowd's guesses estimate the number of jelly beans in a glass vase?
2. Do people who are more confident in their guesses estimate the number of jelly beans differently than people who are less confident?

### Background

Previous research has shown that aggregating non-expert opinions into a collective estimate can produce highly accurate results [1]. One of the most famous examples of this came from statistician Sir Francis Galton. In 1907, Galton asked 787 villagers to guess the weight of an ox at a fair. No one at the fair guessed the correct answer, which was 1197 pounds. But when Galton averaged all of their guesses, the result was 1198 pounds, almost exactly correct [2,3].

The podcast Planet Money recently tried recreating this experiment. They went to a county fair in New Jersey and took pictures of host Jacob Goldstein, who weighed 165 pounds, standing next to a cow, which weighed 1355 pounds, and asked people at the fair and online to guess how much the cow weighed. They ended up receiving 17205 guesses that averaged out to 1287 pounds, which was only about 5% lower than the actual weight. They also asked people who guessed if they were "experts" (i.e., had they ever worked with cows). Interestingly, the average of the "expert" guesses was 1272 pounds, which was a bit worse than the overall crowd [3].

In the Planet Money episode, they interviewed James Surowiecki, a journalist who wrote a book called "The Wisdom of Crowds: Why the Many Are Smarter Than the Few and How Collective Wisdom Shapes Business, Economies, Societies and Nations". He explained that this works because each person is thinking about the problem slightly differently, and each person's guess is contributing some new piece of information. And while each person's guess will introduce some error, these errors tend to cancel out [3]. Another way to look at this would be to invoke the law of large numbers--if individual estimation errors are unbiased and center at the true value, then the average of individual estimations will tend to converge to the true value as the number of individual estimations increases [1].

However, individual estimation errors are not always unbiased or centered at the true value. In the Planet Money episode, Surowiecki explained a phenomenon from behavioral economics called information cascade, where people who are connected by a network influence each other's decisions and behavior and make the same decisions in a sequential fashion [4]. Some examples of this would be stock market panics or bubbles [3]. In their paper "Counteracting estimation bias and social influence to improve the wisdom of crowds," Kao et al. explained that, in addition to error arising from information sharing among individuals, there are also a variety of cognitive and perceptual biases that can influence individual guesses. For example, individuals might systematically overestimate or underestimate due to phenomena such as Stevens' power law, where there is a nonlinear relationship between the subjective perception and actual magnitude of a physical stimulus [1]. Another example is Fechner's law, which states that subjective sensation of a stimulus is proportional to the logarithm of the stimulus intensity [5], implying that lognormal, rather than normal, distributions of estimations are common [1]. Other research studies have shown a tendency for people to underestimate true values in numerosity estimation tasks [6-8].

### Data

To set up this experiment, 1534 jelly beans were placed in a glass vase. Several pictures of the vase were taken from different angles. These pictures were then compiled with this survey. The survey asks respondents to guess the number of jelly beans in the vase, estimate how many minutes they spent thinking before deciding on their guess, and rating their confidence level in their guess on a scale of 1 to 5, with 1 being not confident at all and 5 being completely confident. The last two questions were designed to measure how "expert" someone's guess was. While there likely aren't many jelly bean estimation experts out in the world, the time spent thinking and the person's subjective confidence level might help identify "expert" guesses. To reduce the chances of non-honest or repeat guesses, Google login was required in order to answer the survey.

The survey was posted on the r/SampleSize subreddit on reddit.com and on Facebook, where it gathered 126 responses. The resulting data contains four columns:

* <b>Timestamp:</b> The date and time that a respondent answered the survey.
* <b>How many jelly beans are in the vase?:</b> The respondent's guess of how many jelly beans are in the vase.
* <b>To the nearest minute, how many minutes do you estimate you spent thinking before you decided on your guess?:</b> The respondent's estimation of how long they spent thinking before deciding on their guess.
* <b>On a scale of 1 to 5, with 1 being not confident at all and 5 being completely confident, how confident are you in your guess?:</b> The respondent's rating of their confidence level in their guess.

### Project Organization and Methodology

To answer the project questions, bootstrap hypothesis tests were performed on both the means and medians of the data. The project code is broken into four parts:

* The data folder contains the original data collected from the survey.
* The cleaning_and eda.ipynb file contains the code used to clean and explore the data, with the goal of focusing on questions and methods for further analysis.
* The jellybeans.ipynb file contains bootstrap hypothesis tests on the data, as well as discussion of the background, data, methods, and results of the analysis.
* The requirements.txt contains all the necessary packages and versions to recreate the virtual environment for this project.

### Results

Bootstrap hypothesis tests were performed at a significance level of α = 5% on both the means and medians of the data. Testing the equality of the overall mean guess (1538) and the actual number of jelly beans (1534) yielded a p-value of 0.87, failing to reject the null hypothesis that the mean was equal to 1534. However, testing the equality of the overall median guess (750) and the actual number of jelly beans yielded a p-value of 0, thus rejecting the null hypothesis that the median was equal to 1534. This large difference in results was likely due to the influence of extreme outlier guesses on the mean. When testing the equality of the mean estimates from more confident and less confident guessers, the p-value was 0.58, failing to reject the null hypothesis that the means were the same. Similarly, testing the equality of the median estimates from more confident and less confident guessers, the p-value was 0.24, failing to reject the null hypothesis that the medians were the same.

### References

1. Kao AB, Berdahl AM, Hartnett AT, Lutz MJ, Bak-Coleman JB, Ioannou CC, Giam X, Couzin ID. 2018 Counteracting estimation bias and social influence to improve the wisdom of crowds. J. R. Soc. Interface 15: 20180130. http://dx.doi.org/10.1098/rsif.2018.0130.
2. Yong E. January 31, 2013, 'The Real Wisdom of the Crowds'. National Geographic. https://www.nationalgeographic.com/science/article/the-real-wisdom-of-the-crowds.
3. April 17, 2019, 'How Much Does This Cow Weight?' Planet Money. https://www.npr.org/transcripts/714289051.
4. Easley D, Kleinberg J. Networks, Crowds, and Markets: Reasoning about a Highly Connected World. Cambridge University Press (2010). https://www.cs.cornell.edu/home/kleinber/networks-book/networks-book-ch16.pdf
5. Jeans J (1968/1937). Science & Music. Dover Publications.
6. Izard V, Dehaene S. 2008 'Calibrating the mental number line'. Cognition 106, 1221–1247. https://www.unicog.org/publications/IzardDehaene_NumerosityNamingCalibration_Cognition2007.pdf.
7. Krueger LE. 1982 'Single judgments of numerosity'. Atten. Percept. Psychophys. 31, 175–182. https://link.springer.com/content/pdf/10.3758/BF03206218.pdf.
8. Krueger LE. 1984 'Perceived numerosity: a comparison of magnitude production, magnitude estimation, and discrimination judgments'. Atten. Percept. Psychophys. 35, 536–542.https://link.springer.com/content/pdf/10.3758/BF03205949.pdf.
