# Vladislavs Fedins 221RDB416
def parallel_processing(num_threads, num_jobs, job_times):
    out = []
    finish_times = [0] * num_threads
    for job_idx, job_time in enumerate(job_times):
        earliest_finish_time = min(finish_times)
        earliest_finish_thread = finish_times.index(earliest_finish_time)
        
        out.append((earliest_finish_thread, earliest_finish_time))
        finish_times[earliest_finish_thread] += job_time
        
    return out

def main():
    a, b = map(int, input().split())
    data = list(map(int, input().split()))
    res = parallel_processing(a, b, data)
    for z, c in res:
        print(z,c)

if __name__ == "__main__":

    main()
