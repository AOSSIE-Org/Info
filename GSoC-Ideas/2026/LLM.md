# End-to-End Open-Everything Verifiable LLM

## Background and Motivation

In 2025 we had many projects that used LLMs and we ended depending on LLMs that were closed-source, paid, privately trained... 
Even when there are models where the weights are open, it is often unclear which data has been used to train the models privately.

As people rely more and more on LLMs to get answers for their questions, 
there will be more and more incentive for LLM providers to bias their models in favour of their own views or 
in favour of the views of their sponsors and advertisers.  The world will need impartial LLMs, 
trained or fine-tuned by a neutral organization, trained on a reliable and neutral source of knowledge
and trained in an open, deterministic and reproducible way, so that anyone can independently verify that 
the resulting model was indeed trained/fine-tuned on the claimed training data, 
and trained/fine-tuned using only open data and open libraries/tools.

This state of affairs motivates us to propose implementing a pipeline to train from scratch what would be, 
to our knowledge, the first end-to-end open-everything verifiable LLM


## Overview of Tasks

* Implement a pipeline that could be used to easily train an completely untrained LLM (to ensure complete transparency about training) on publicly available neutral dataset that anyone can access and replicate today establishing a verifiable baseline free from hidden biases or ephemeral datasets.
* Use this pipeline to train LLMs with sizes suitable to be used by our own projects, including compact models optimized for edge deployment on mobile and resource-constrained devices.
* Implement a verification protocol to allow anyone to replicate identical model checkpoints, implying that the model was trained on the said data without any hidden training.
* Evaluate trained models on the following success metrics:
    - Bias testing
    - Factual accuracy
    - Performance on standard benchmarks


## Requirements

* Only open-source libraries should be used in the training pipeline.
* Wikipedia should be used as the source of reliable trustworthy data.
* The training algorithms and pipeline should be deterministic: 
  if two people use the pipeline on the same data, they should obtain exactly the same model. 
  This guarantees that people can independently verify that the LLM was trained on the data on which it is claimed to have been trained.
* One of the models trained should be small enough (1B-3B) to be usable as a local mobel in mobile devices for mobile apps.
* The GSoC applicant must draft a well-formatted proposal on Google Docs. The format will be shared by the organisation at the start of the application period.
* The proposal must contain proper diagrams to help us understand how you are going to achieve the above tasks. These diagrams should be made in either Excalidraw or Draw.io.

## Resources

* TODO

## Ideators

* GitHub: @Zahnentferner ; Discord: @b.wp

## Mentors

* GitHub: @Archit381 ; Discord: @archit381_
* GitHub: TODO; Discord: TODO
* GitHub: @Zahnentferner ; Discord: @b.wp

## Communication Channel

Join our Discord servers (https://discord.gg/xnmAPS7zqB and https://discord.gg/fuuWX4AbJt) and discuss this idea in https://discord.com/channels/1022871757289422898/1180497744666837003.
