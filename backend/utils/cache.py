from flask_caching import Cache

cache = Cache(config={'CACHE_TYPE': 'SimpleCache'})

def cache_answer(prompt, pipeline):
    result = cache.get(prompt)
    if result:
        return result
    else:
        generated = pipeline(prompt, max_new_tokens=200)[0]['generated_text']
        answer = generated.split('Answer:')[-1].strip()
        cache.set(prompt, answer, timeout=600)
        return answer
