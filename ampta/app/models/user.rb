class User < ActiveRecord::Base
  # attr_accessible :title, :body
  has_and_belongs_to_many :projects
  has_many :tickets
end
