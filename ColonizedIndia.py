import streamlit as st

st.set_page_config(page_title="India As It Was: Colonization", page_icon="IndianFlag.png", layout="wide")

sb = st.sidebar
sect = sb.radio("Navigation:", ("Homepage", "The Colonizers", "What They Got VS What They Lost", "The Legacy", "Sources"))

if sect == "Homepage":
    
    st.title("India As It Was: Colonization")
    st.write("---")
    st.image("IndianFlag.png", "https://en.wikipedia.org/wiki/Flag_of_India")
    
    write = """
    ***When the British colonized India, everything changed.***
    
    *It started out like any other colonization process the British had gone through; trading, communication where possible, and mutual profit. India got resources and products from Europe, while the British got spices and herbs that became delicacies in Europe.*

    *From the British, India got infrastructure and a new governmental system, as well as more European technology. From India, the British got tea, herbs, spices (like pepper, cardamom, ginger and turmeric) and cotton cloth, with all of this being courtesy of the British East India Company, which was given a monopoly over trading in India by Elizabeth the First in 1600.*

    *This monopoly allowed the British East India Company to grow more and more powerful until it created alliances with Indian rulers and formed its own army to protect itself and its resources; this company also became the first essential*

    *However, as time went on, the British started to insert operatives into the governmental systems of India, and those people started to work their way up, lying and killing when necessary, until they became the controllers of their area. This took place in many Indian kingdoms, until the vast majority were ruled by the British, with all others getting wiped out completely. Once they gained control, they started to force their way of life onto India, stealing resources and workers to make a profit, while making sure that the remaining Indians couldn't continue to make the money they needed to continue living. In short, they became parasites on India.*

    ***This is where it started.***

    *Kids being converted to Christianity, who no longer knew their native language; silk workers' fingers being cut off to prevent them from working; villages and castles were plundered of their valuables; and much more leaving India as a chaotic and unstable country with a corrupt government system and society that would do anything for money, even if it killed.*
    
    *Farmers were underpaid, and a new governmental system was put in place, with tax collectors collecting more money than the farmers could make, leaving little to no money left over for food. These farmers could barely feed themselves, even less their families!*

    *Tax collectors would knock on farmers' doors to collect their taxes, and when the farmers couldn't pay, they would often get beat up. Farmer parents would often commit suicides just to get compensation that could pay debts and taxes for some time, before debt came back to haunt them once more. If they couldn't pay, their land would get taken away, tanking their chances of paying their bills even further.*
    
    *If farmers dared to retailate, they would often be arrested or shot, preventing the families from making enough money to continue. Besides suicides, disease and medical bills would continue to take even more lives, while the power-hungry government would ruthlessly deal with them without remorse or any form of mercy. The government would also, when asked what they were doing, ramble on about "all the work" they were doing, when in reality, they were just finding ways to make more and more money, while doing less and less work, at the cost of the lower-class society.*
    
    *Later on, the police force would grow to be riddled with corrupt cops, who would be paid by gangs to ensure their safety, no matter what crimes they committed, while arresting those that the gangs didn't like, and finding reasons to do so. Even now, they still try to find reasons to arrest whoever they can, and may be paid by large gangs to do so.*

    *Currently, India has recovered a decent bit, but still continues to be a somewhat chaotic and disorganized country, with many roads being badly built (some not at all), and toll gates everywhere from money-grabbing corporations who buy the roads to make money off of citizens that try to pass by.*

    *Without European intervention, India could have grown to be a largely successful and powerful country, and this is likely what the British were afraid of when they ransacked India for all it's resources and goodwill.*
    """

    st.write(write)

if sect == "The Colonizers":
        
    write = """
    The British Empire is known to have been a country of piracy, stealing from other lands and taking credit of them as their own.

    From India, they stole precious gems and minerals, as well as their forms of cuisine and agriculture; one of the most iconic being tea. Tea is considered to represent the British, but the reality is, they had stolen tea - as well as the methods of brewing it - from India and China, and taken credit for it as their own.
    
    When colonizing a country, their goal is to make as much of a profit as possible before preventing any recovery of the targeted country, essentially draining the country of its resources and skilled workers until it no longer has hope of bouncing back.

    This allows for maximum profit for Britain, while preventing any sort of retailiation from the target country, and often committing genocides in the process.
    """
        
    st.title("The British Empire")
    st.write("---")
    st.image("BritishFlag.jpg", "https://www.britannica.com/topic/flag-of-the-United-Kingdom")
    st.write(write)

if sect == "What They Got VS What They Lost":
    
    st.title(sect)

    c1, c2 = st.columns(2)
    ex1, ex2 = c1.expander("What They Got"), c2.expander("What They Lost")
    got = """
     - **Exposure to British Culture and Christianity**; Christian schools were built on Indian land, as a (somewhat successful) attempt to assimilate Indians into Christianity.
     - **British Technology and Knowledge**; they had brought their own technology, but had destroyed or buried Indian knowledge and tradition to be replaced with that of the British.
     - **British Infrastructure**; they had built roads, railroads and modern buildings, but had brought an end to traditional Indian construction methods, which had resulted in many ancient engineering wonders, which are still standing and visited to this day - especially temples, which have been built in ways that are simply hard to fathom with our current understanding of science, including the Brihadeeswara Temple, which was built in such a way that it does not cast a shadow at any time of day.
    """    
    lost = """
     - **Jewelery and Precious Metals**; diamonds, rubies, and many other gems were stolen from the mineral-rich land of India.
     - **The Koh-i-Noor Diamond (*now in Queen Elizabeth's crown*)**; a rare and precious diamond believed to be revered by the Indian gods themselves. This diamond was also believed to curse anyone who possessed it with bad luck, which was said to be seen with the past people who have had it. This diamond was stolen by the British as a "treasure of conquest", and was made into a part of Queen Elizabeth's crown. The crown was laid on her coffin after she died, and the diamond has not been returned to this day.
     - **Many Profitable Skills and Goods**; silks, jewelery, farming, herbal medicine, etc.)
     - **Cultural Identity**; diminished the trusting and interconnected way of life in India, creating greater conflict
     - **Goodwill**; currently, people are often hostile and power-hungry, as well as greedy and inconsiderate, especially in higher social classes
     - **Valuable Resources**; minerals, textiles and cloths, plants/herbs, etc.
     - **Religion**; similar to residential schools, [the British] built Christian schools and churches to assimilate Indians from their many religions (Hinduism, Buddhism, Jainism, etc.) to Christianity
    """

    ex1.write(got)
    ex1.title("")
    ex2.write(lost)
    ex2.title("")

    c1, c2 = st.columns(2)
    
    c1.image("Koh-I-Noor.jpg", "https://www.baunat.com/en/what-is-the-koh-i-noor-how-much-is-this-stone-worth")
    c2.image("GandhiSpinner.jpg", "https://silkroadgallery.co.uk/blogs/news/traditional-spinning-wheel-information")

if sect == "The Legacy":
    
    write1 = """
Gangs in India are quite common, especially in bigger cities, where a better economy is present, which is often supported by drug
cartel, weapons distribution and human trafficking. This acts as an incentive for political figures to support these operations,
despite any illegal aspects that they "might" have. This came as a result of both the greed of higher-class people, and the introduction
of money from the British, which would only serve to boost the effect of this illegal business, creating a thriving black market that
could not be stopped by the police, either because the gangs were supporting them financially, or because they were
simply too powerful. Most gangs (particularly well-rooted gangs) use 1 or more of 3 methods to stay in operation - they would:
manipulate the public into thinking that they are the "good guys", and that they were responsible for keeping others safe and living
comfortably (even though they were often responsible for many killings and raids); use business as an incentive for the government and
police force to avoid conflict with them, often bribing officers and political figures for protection from the justice system (which is
ironic, at this point); or they may legitmetely be trying to help people through whatever methods they can - they often were still
illegal, but they would try to stray from harming innocent people, and target those who were already rich, and were misusing their
power; a Robin Hood-type scenario. Unfortunately, the first 2 tend to be the most common, and these gangs are only growing due to them
advertising protection to young adults, teenagers, and sometimes even ***children***, only for them to find out that the "protection"
was from enemy gangs, and if they were to refuse orders or leave, they would often be hunted down and killed, sometimes being tortured
prior to their death. This might happen in front of the gang to set an example of what would happen if you "betrayed" the gang, keeping
the others in and trapping them in a cycle of crime, minimal payment and extremely limited chances of living a normal life.
"""

    write2 = """
The leaders of India after it gained independence were often power-hungry and money-minded; they could be bought into illegal businesses, where
gangs would pay them to "overlook" the gang's operations, and sometimes providing police security for these operations in black market
industries like human trafficking, drug distribution and the dealing of firearms. This was likely due to the British's greed for
land and power, with India being one of the victims, and they left behind a political system filled with people that cared about
power and resources over the good of the people. However, recently, these things have started to die down, and India is in the
process of becoming less corrupt and developing towards a stronger country, though it will likely not be able to do this on its
own, but rather with the help of other countries.
"""
    write3 = """
After the British left, money-grabbing corporations ran rampant; often they would side with large gangs to increase their income while
offering protection and resources to the gangs. Insurance companies would often charge the poor more than the rich, as the rich had assets
to offer, while the poor would keep paying. They would also bribe political figures and police for protection and for them to ignore
any illegal procedures they may be using, which created lots of conflict between large companies and the public. This was likely
due to the popularization of money by the British, as opposed to fair trade. This meant that the power-hungry higher-class of India
would always look for ways to make money, no matter who it harmed, which - half the time - would end in bribery and illegal activity,
fueling the conflict between them and the public.
"""

    st.title(sect)

    ex1 = st.expander("Gang Operations and Violence")

    c1, c2 = st.columns(2)
    ex2, ex3 = c1.expander("Corrupt Political Figures"), c2.expander("Money-Grabbing Corporations")

    ex1.subheader("Gang Operations and Violence")
    ex1.write(write1)

    ex2.subheader("Corrupt Political Figures")    
    ex2.write(write2)

    ex3.subheader("Money-Grabbing Corporations")
    ex3.write(write3)

if sect == "Sources":

    src = """
     - *Henneberg, Susan. The Religion and Beliefs of Ancient India, Rosen Publishing, p. (Summary).*    
     - *“British Raj.” Encyclopedia Britannica, Encyclopedia Britannica, inc., 1 Mar. 2024, www.britannica.com/event/British-raj.*
     - *Magazine, Smithsonian. “The True Story of the Koh-i-Noor Diamond-and Why the British Won’t Give It Back.” Smithsonian.Com, Smithsonian Institution, 30 Aug. 2017, www.smithsonianmag.com/history/true-story-koh-i-noor-diamondand-why-british-wont-give-it-back-180964660/*
    """

    st.title(sect)    
    st.write(src)
