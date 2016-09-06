# ===============================================================================
# Copyright 2016 ross
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ===============================================================================

# ============= standard library imports ========================
# ============= local library imports  ==========================

# task1
p1 = '/Users/ross/Desktop/p1.txt'
p2 = '/Users/ross/Desktop/p2.txt'

p1file = open(p1, 'r')
p2file = open(p2, 'w')

for li in p1file.readlines():
    p2file.write(li)

# task2
p1 = '/Users/ross/Desktop/p1.txt'
p2 = '/Users/ross/Desktop/p2.txt'

p1file = open(p1, 'r')
p2file = open(p2, 'w')

cnt = 0
for li in p1file.readlines():
    if cnt == 0:
        p2file.write(li)
    else:
        items = li.split(',')
        p2file.write(items[0]+','+items[1] + ',' + items[2])


# ============= EOF =============================================
