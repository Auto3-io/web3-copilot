def copilot(user_requirement: str):
    overall_steps = task_interpreter(user_requirement) # Step with protocol, chain
    search_result = method_search_engine(overall_steps, db.methods) # + contract, method

    completed_steps = complete_step(search_result, db.contracts, db.tokens) # + address
    summarized_steps = summarizer(user_requirement, search_result) # summrize

    program = program_generator(summarized_steps)