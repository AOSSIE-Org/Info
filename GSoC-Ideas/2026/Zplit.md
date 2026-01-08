# Zplit

## Background and Motivation
While there are a number of Applications available today that offer the functionality to split group finances between users for easy tracking and settlement, the most popular ones leave a lot of features to be desired, and are closed source. 

Moreover, these apps follow a FreeMium model, meaning that of the limited features that do exist, the best ones are often locked behind paywalls.

Zplit was ideated to solve this very issue, because keeping track of you finances and transactions shouldn't require you to make more transactions.

Zplit is an open source new age group transaction tracking solution, that uses a completely decentralized model for data transfer. This means that you are always in control of your data, and never have to pay for any features. 
It features a modern and minimalistic design for the average consumer, with advanced capabilities like Expense Tracking and useful data visualisations for all your expenses.

## Overview of Tasks

#### Complete UI Implementation for Zplit
AOSSIE recently invited contributors to submit designs for Zplit. While Zplit is going to follow a modular approach with respect to the UI (i.e: Different Themes of Zplit will completely change how the App looks, rather than just the color), we selected [this](https://github.com/StabilityNexus/Zplit/blob/dev/design/zplit-design.fig) as the base design to start with. It is required to complete implementing this UI, by making all remaining screens.
#### Implement Selected Data Model and State Management
AOSSIE had a discussion about Data Models for Zplit [here](https://github.com/StabilityNexus/Zplit/issues/19). It is required to implement the selected Data Model using `freezed` and codegen, and then implement app-wide State Management using `BLoC`. This should be done in a decoupled manner, with Automated Tests in mind, and should be reliable and robust.
#### Write decentralized communication algorithms
As Zplit uses decentralized methods for all of it's data transfer, it is required to write the business logic (aka algorithms) that the application will use to send and recieve data. There will be multiple methods and options for the end user as described in the [Zplit Repo](https://github.com/StabilityNexus/Zplit/blob/main/zplit.md). These will need to be implemented from scratch, preferrably using strongly typed Dart code. Using packages where available is allowed and preferred.
#### Write Tests for all functionalities
Zplit will follow a Test Driven Development workflow, where Contributors will be expected to write comprehensive tests for every feature they implement. This will be to reduce the risk of changes affecting pre-existing features and will save maintainer effort and time. These tests should use official Flutter packages for Testing and Mocking.
#### Setup CI/CD Pipelines for automated builds and tests
It is necessary to implement CI/CD Pipelines that can automate the build and release process, as well as add a check for every PR to verify that all changes pass the tests. Along with this, other Workflows will also be expected, to improve Developer Experience, like a workflow to check for untranslated strings after every PR. These workflows will be implemented using GitHub Actions.
#### Deploy v1 of Zplit to Play Store
GSoC 2026 Contributions should conclude with a v1 deployment of Zplit to App Stores, to get the app to real users as soon as possible, and then later iterate on the App with real world feedback from users. AOSSIE already has a Play Store Developer Account, so the Candidate will be required to setup the new application here, along with filling all data safety questionairres etc., and fulfilling all publishing requirements.

Candidates are expected to refine these tasks in their GSoC proposals.

## Requirements

* No paid/freemium external dependencies should be used anywhere
* Zplit should have all basic features implemented by the end of the Coding Period
* Zplit should be deployed on the App Stores by the end of the coding period
* All Workflows should be running by the end of the coding period


## Resources

* [Zplit.md](https://github.com/StabilityNexus/Zplit/blob/main/zplit.md)
* [Zplit README](https://github.com/StabilityNexus/Zplit/blob/main/README.md)
* [BLoC Documentation](https://bloclibrary.dev/)
* [pub.dev](pub.dev)

## Ideators

* GitHub: @Zahnentferner ; Discord: @b.wp
* GitHub: @M4dhav; Discord: @m4dhav

## Mentors

* GitHub: @Zahnentferner ; Discord: @b.wp
* GitHub: @M4dhav; Discord: @m4dhav

## Communication Channel

Join our Discord servers (https://discord.gg/xnmAPS7zqB and https://discord.gg/fuuWX4AbJt) and discuss this idea in (https://discord.com/channels/1022871757289422898/1438097765887643709).
