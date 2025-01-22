import os
import re

# File 1
# open exam.log file
with open("exam.log", 'r') as file:
    file_lines = file.readlines()

    # write ip_result function
    def ip_result(file_lines):
        
        # prep variables for use below
        ip_list = []
        ip_uniqe_list = []
        ip_count = {}
        
        # search for ip's (regex)
        for line in file_lines:
            match = re.search("\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3}", line)
            if match:
                ip_list.append(match.group(0))
                
        # counts number of ip's
        # put result in dict
        ip_unique_list = set(ip_list)
        
        for ip in ip_unique_list:
            if ip not in ip_count.keys():
                ip_count[ip] = ip_list.count(ip)
        
        # sort ip_count dict from lowest to highest ip (not specified if sort should be IP- or activity count-based)
        sorted_ip_count = dict(sorted(ip_count.items()))
        
        # return dict to use in file write of ip_count.txt
        return sorted_ip_count

# puts ip_result into a file  
with open("ip_count.txt", 'a') as outfile:
    outfile.write("IP Address Count:\n\n")
    
    # get sorted dict of IP count
    ip_dict = ip_result(file_lines)
    
    # add to ip_count.txt
    for key, value in ip_dict.items():
        outfile.write(f"{key}: {value}\n")
# End File 1


# File 2
## open exam.log
with open("exam.log", 'r') as file:
    file_lines = file.readlines()

    # write invalid_user_count function
    def invalid_user_count(file_lines):
        
        # prep variables for use below
        invalid_user_list = []
        unique_invalid_user_list = []
        invalid_user_count = {}
        
        # search for invalid users, create list
        for line in file_lines:
            match = re.search("Invalid user ([a-zA-Z0-9]+) ", line)
            if match:         
                invalid_user_list.append(match.group(0).strip().split()[2])
        
        # counts invalid logins for each unique user
        unique_invalid_user_list = list(set(invalid_user_list))

        # counts number of invalid logins by user
        # put result in dict
        for user in unique_invalid_user_list:
            if user not in invalid_user_count.keys():
                invalid_user_count[user] = invalid_user_list.count(user)

        # sort the dict by number of attempts (highest to lowest)
        sorted_invalid_user_count = dict(sorted(invalid_user_count.items(), key=lambda item: item[1], reverse=True))

        return sorted_invalid_user_count
        
# puts invalid_user_count into a file  
with open("invalid_user_count.txt", 'a') as outfile:
    outfile.write("Invalid Users by # of Attempts:\n\n")
    
    # get sorted dict of IP count
    invalid_user_dict = invalid_user_count(file_lines)
    
    # add to invalid_user_count.txt
    for key, value in invalid_user_dict.items():
        outfile.write(f"{key}: {value}\n")
# End File 2

        
# File 3
# open exam.log
with open("exam.log", 'r') as file:
    file_lines = file.readlines()

    # write invalid_user_count function
    def failed_logins(file_lines):
        
        # prep variables for use below
        failed_logins_list = []
        failed_logins_ip_list = []
        unique_failed_logins_ip_list = []
        failed_logins_count = {}
        
        # search for failed authentication, create list
        for line in file_lines:
            match_auth_fail = re.search("authentication failure;", line)
            if match_auth_fail:         
                failed_logins_list.append(line)
        
        # take failed auth list and pull ip's        
        for line in failed_logins_list:
            match_ip = re.search("\d{1,3}\.\d{1,3}\.\d{1,3}.\d{1,3}", line)
            if match_ip:
                failed_logins_ip_list.append(match_ip.group(0))

        # create list to filter unique ip's
        unique_failed_logins_ip_list = list(set(failed_logins_ip_list))
        
        # counts failed logins
        # put result in dict
        for ip in unique_failed_logins_ip_list:
            if ip not in failed_logins_count.keys():
                failed_logins_count[ip] = failed_logins_ip_list.count(ip)

        # sort dict
        sorted_failed_logins_count = dict(sorted(failed_logins_count.items(), key=lambda item: item[1], reverse=True))

        return sorted_failed_logins_count
        
# puts failed_logins into a file  
with open("failed_login_attempts.txt", 'a') as outfile:
    outfile.write("Failed Login Attempts by IP:\n\n")
    
    # get sorted dict of failed login IP count
    failed_login_dict = failed_logins(file_lines)
    
    # add to invalid_user_count.txt
    for key, value in failed_login_dict.items():
        outfile.write(f"{key}: {value}\n")
# End File 3
